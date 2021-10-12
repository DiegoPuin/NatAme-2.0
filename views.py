from http import HTTPStatus
from flask import Blueprint, Response, request, render_template, url_for, redirect, flash
from werkzeug.wrappers import response
import json
from querys import *

home = Blueprint("home", __name__, url_prefix="/home")
shopCart = Blueprint("shopcart", __name__, url_prefix="/shopcart")
shopBag = Blueprint("shopbag", __name__, url_prefix="/shopbag")
categories = Blueprint("categories", __name__, url_prefix="/categories")
login = Blueprint("login", __name__, url_prefix="/login")
register = Blueprint("register", __name__, url_prefix="/register")
stadistics = Blueprint("stadistics", __name__, url_prefix="/stadistics")
regions = Blueprint("regions", __name__, url_prefix="/region")
users = Blueprint("user", __name__, url_prefix="/user")
register_cliente = Blueprint("register_cliente", __name__, url_prefix="/register_cliente")
factura = Blueprint("factura", __name__, url_prefix="/factura")
shopCart2 = Blueprint("shopcart2", __name__, url_prefix="/shopcart2")
pago = Blueprint("pago", __name__, url_prefix="/pago")

conexion = None
dict={}

@home.route('/<string:name_region>', methods=["GET"])
def change_region(name_region):
    info = {"region": name_region}
    return render_template('home.html', info=info)


@factura.route("/", methods=["GET"])
def show_product():
    long_item_fact=[]
    conexion = connect()
    USER_DATA["k_identificacion"]=21112
    dict['factura']= conexion.sentenciaFuncion('FU_FACTURA_VENTA',[USER_DATA["k_identificacion"],0, "null"])
    dict['item_factura']= conexion.sentenciaFuncion('FU_ITEM_FACTURA',[0, "null"])
        #dict['factura'] = datos
        #factura.append(datos)
    #dict['factura']['id_c'] = factura[0]
    #print('datos fun: ',dict['factura'])
    print('datos fun: ',dict['item_factura'])
    for i in range(len(dict['item_factura'])):
        long_item_fact.append(i)
    dict['long_item_fact']=long_item_fact    
    return render_template('factura.html',dict=dict)


@shopBag.route("/", methods=["GET","POST"])
def show_product():
    long_pedidos=[]
    conexion = connect()
    id_ped=[]
    fecha_ped=[]
    precio_ped=[]
    tid_ped_rep=[]
    id_ped_rep=[]
    cal_ped=[]
    comentarios=[]
    USER_DATA["k_identificacion"]=21112
    print(conexion.sentenciaFuncion('FU_PEDIDOS',[USER_DATA["k_identificacion"],0, "null"]))
    for datos in conexion.sentenciaFuncion('FU_PEDIDOS',[USER_DATA["k_identificacion"],0, "null"]):
        id_ped.append(datos[0])
        fecha_ped.append(datos[1])
        precio_ped.append(datos[2])
        tid_ped_rep.append(datos[3])
        id_ped_rep.append(datos[4])
        cal_ped.append(datos[5])
        comentarios.append(datos[6])
    dict['pedidos']= {"id_ped":id_ped,"fecha_ped":fecha_ped,"precio_ped":precio_ped,"tid_ped_rep":tid_ped_rep,"id_ped_rep":id_ped_rep,"cal_ped":cal_ped, "comentarios":comentarios}
    
    
        #factura.append(datos)
    #dict['factura']['id_c'] = factura[0]
    #print('datos fun: ',dict['factura'])
    print('datos fun: ',dict['pedidos'])
    print("id",dict['pedidos']['id_ped'][0])
    for i in range(len(dict['pedidos']['id_ped'])):
        long_pedidos.append(i)
    dict['long_pedidos']=long_pedidos

    if request.method=='POST':
        dat = request.form
        print('datos pago:', dat)
        clave=[]
        valor=[]
        for key,value in dat.items():
            #print(key," : ", value)
            clave.append(key)
            valor.append(value)
        dict['calificar']={"clave":clave,"valor":valor}
        #print ("Cambios:", dict['calificar'] )
        #print ("Cambios:", dict['calificar']['clave'][9] )
        print(len(dict['pedidos']['id_ped'])*2+1)

        for i in range(0,len(dict['pedidos']['id_ped'])*2-1,2):  
            print(("update calificacion_pedido set q_calificacion ="+dict['calificar']['valor'][i]+", n_comentarios ='"+dict['calificar']['valor'][i+1]+"' where k_pedido="+dict['calificar']['clave'][i]))
            conexion.sentenciaSimple("update calificacion_pedido set q_calificacion ="+dict['calificar']['valor'][i]+", n_comentarios ='"+dict['calificar']['valor'][i+1]+"' where k_pedido="+dict['calificar']['clave'][i])
        conexion.commint()
            

        return render_template('shopbag.html',dict=dict)

    
    return render_template('shopbag.html',dict=dict)


@pago.route("/", methods=["GET","POST"])
def show_product():
    conexion = connect()
    consulta1 =[]
    consulta2=[]
    longitud_m_pago=[]
    USER_DATA["k_identificacion"]=21112
    #SELECT pr.n_nomproducto, i.v_precio_unidad FROM PAIS p, REGION r, PRODUCTO pr, INVENTARIO i WHERE UPPER(p.n_nombre_pais)='COLOMBIA' AND p.k_pais=r.K_pais AND UPPER(r.n_nombre_region)='CARIBE' AND i.k_pais=r.K_pais AND i.k_region=r.k_region AND i.k_producto=pr.k_producto   
    #for datos in conexion.sentenciaCompuesta(" select u.n_usuario, m.n_detalle_metodo_pago from metodo_de_pago m, cliente c, usuario u  where c.k_identificacion=m.k_identificacion_cli and u.k_identificacion='21113'and u.k_identificacion=c.k_identificacion"):
    for nombre,apellido,tipoid, id  in conexion.sentenciaCompuesta(" select u.n_nombre, u.n_apellido, u.k_tipoid, u.k_identificacion from usuario u  where u.k_identificacion="+str(USER_DATA["k_identificacion"])):
    #for datos in conexion.sentenciaCompuesta(" select * from tipo_de_pago "):
        dict['usuario'] = {"nombre":nombre,"apellido":apellido,"tipoid":tipoid, "id":id}
        #consulta1.append(datos[0])
        #consulta2.append(datos[1])
    for datos in conexion.sentenciaCompuesta(" select k_tipopago, n_descripcion from tipo_de_pago "):
        consulta1.append(datos[0])
        consulta2.append(datos[1])

    
    
    dict['pago'] = {"id":consulta1, "t_pago":consulta2}
    for i in range(len(dict['pago']['id'])):
        longitud_m_pago.append(i)
    dict['longitud_m_pago']= longitud_m_pago
        
    
        
    #print (consulta1)  
    #nombre=consulta1[0]
    print  (dict)
    consulta3=[]
    #if request.method=='POST':
    #for datos in conexion.sentenciaCompuesta(" select k_clienterep from representante_cliente rc, cliente c, usuario u where rc.i_tipoid_cli=c.k_tipoid and rc.q_identificacion_cli= c.k_identificacion and u.n_usuario='"+ str(nombre) + "' and c.k_tipoid=u.k_tipoid and c.k_identificacion=u.k_identificacion"):
    #    consulta3.append(datos[0])
    #print(consulta3)

    m_pago=[]
    m_pagoname=[]
    #dict['medio_pago']={"m_pago":m_pago,"m_pagoname":m_pagoname}

    if request.method=='POST':
        dat = request.form
        print('datos pago:', dat)
        for key,value in dat.items():
            #print(key," : ", value)
            if value !='0':
                dict['medio_pago']={"m_pago":key,"m_pagoname":value}
                #m_pago.append(key)
                #m_pagoname.append(value)
                #cantidad.append(value)
        print(dict['medio_pago'])
        #conexion.sentenciaSimple('Insert into tipo_de_pago(K_TIPOPAGO,N_DESCRIPCION) values ('3',to_char (sysdate,'DD/MM/YYYY')) ')
        total =str(dict['total'])
        print(total)
        conexion.sentenciaSimple("Insert into pedido(F_PEDIDO,  I_ESTADO, Q_VALORT, K_TIPOID, K_IDENTIFICACION ) values (sysdate,'PAG','"+str(dict['total'])+"','"+str(dict['usuario']['tipoid'])+"','"+str(dict['usuario']['id'])+"')")
        
        conexion.commint()
        pedido=[]
        for datos in conexion.sentenciaCompuesta(" select seq_pedido_k_pedido.currval from dual"):
            pedido.append(datos[0])
        ped=pedido[0]
        dict['pedido']=ped
        print('pedido: ',str(dict['pedido']))
        print(str(dict['medio_pago']['m_pago']))

        conexion.sentenciaSimple("Insert into pago_pedido(K_PEDIDO,K_PAGO_PEDIDO, K_TIPOPAGO, F_PAGO,V_PAGO,I_ESTADO)  values ('"+str(dict['pedido'])+"','1','"+ str(dict['medio_pago']['m_pago'])+"',sysdate,'"+str(dict['total'])+"','AUT')")
        conexion.sentenciaSimple("Insert into calificacion_pedido(K_PEDIDO) values("+str(dict['pedido'])+")")
        region=[]
        for datos in conexion.sentenciaCompuesta("select r.k_region from representante r, representante_cliente rc where rc.k_identificacion_cli='"+ str(dict['usuario']['id'])+"' and r.k_identificacion=rc.k_identificacion_rep "):
            region.append(datos[0])
        reg=region[0]
        dict['region']=reg
        print(dict['categoria_1'])
        
        for i in range(len(dict['categoria_1']['nombre'])):
            id=dict['categoria_1']['id'][i]
            print('id:',id)
            conexion.sentenciaSimple("Insert into item(K_PEDIDO,K_ITEM, Q_CANTIDAD, V_PRECIO, K_PAIS, K_REGION, K_PRODUCTO ) values ('"+str(dict['pedido'])+"','"+ str(i+1) +"','"+ str(dict['compra']['cantidad'][i])+"','"+str(dict['categoria_1']['total'][i])+"','1','"+str(dict['region'])+"','"+ str(dict['categoria_1']['id'][i])+"')")
        conexion.commint()
        return render_template('confirmacion_pago.html', dict=dict) 
        
    
    
    return render_template('pago.html', dict=dict) 
    #consulta1=nombre,consulta2=consulta2)


######################## Metodos para las rutas de shopcart ######################################

@shopCart2.route("/", methods=["GET","POST"])
def show_product():
    producto=[]
    cantidad=[]
    compra={'producto':producto,'cantidad':cantidad}
    if request.method=='POST':
        dat = request.form 
        for key,value in dat.items():
            #print(key," : ", value)
            if value !='0':
                producto.append(key)
                cantidad.append(value)
        print(compra)
        return render_template('home.html')
    print("entro")
    return(compra)

@shopCart.route("/", methods=["GET","POST"])
def show_product():
    '''
    #Funciona
    conexion = connect()
    consulta1 =[]
    consulta2 =[]
    
    for datos in conexion.sentenciaCompuesta("SELECT i.v_precio_unidad FROM PAIS p, REGION r, PRODUCTO pr, INVENTARIO i WHERE UPPER(p.n_nombre_pais)='COLOMBIA' AND p.k_pais=r.K_pais AND UPPER(r.n_nombre_region)='CARIBE' AND i.k_pais=r.K_pais AND i.k_region=r.k_region AND i.k_producto=pr.k_producto"):
        consulta1.append(datos[0])
      
    for datos in conexion.sentenciaCompuesta("SELECT pr.n_nomproducto FROM PAIS p, REGION r, PRODUCTO pr, INVENTARIO i WHERE UPPER(p.n_nombre_pais)='COLOMBIA' AND p.k_pais=r.K_pais AND UPPER(r.n_nombre_region)='CARIBE' AND i.k_pais=r.K_pais AND i.k_region=r.k_region AND i.k_producto=pr.k_producto"):
        consulta2.append(datos[0])
   
    categoria= {'precio':consulta1,'nombre':consulta2}
    #precio= consulta["precio"]
    longitud=[]
    for i in range(len(categoria["nombre"])):
        longitud.append(i)
    print(longitud)
    #categoria=consulta["precio"]
    return render_template('shopcart.html',categoria=categoria,longitud=longitud)
    '''
    conexion = connect()
    consulta1 =[]
    consulta2 =[]  
    consulta3 =[]
    #SELECT pr.n_nomproducto, i.v_precio_unidad FROM PAIS p, REGION r, PRODUCTO pr, INVENTARIO i WHERE UPPER(p.n_nombre_pais)='COLOMBIA' AND p.k_pais=r.K_pais AND UPPER(r.n_nombre_region)='CARIBE' AND i.k_pais=r.K_pais AND i.k_region=r.k_region AND i.k_producto=pr.k_producto   
    for datos in conexion.sentenciaCompuesta(" SELECT  pr.n_nomproducto, i.v_precio_unidad, i.K_PRODUCTO FROM PAIS p, REGION r, PRODUCTO pr, INVENTARIO i WHERE UPPER(p.n_nombre_pais)='COLOMBIA' AND p.k_pais=r.K_pais AND UPPER(r.n_nombre_region)='CARIBE' AND i.k_pais=r.K_pais AND i.k_region=r.k_region AND i.k_producto=pr.k_producto order by pr.n_nomproducto asc"):
        consulta1.append(datos[0])
        consulta2.append(datos[1])
        consulta3.append(datos[2])
    #print (consulta1)  
    categoria= {'nombre':consulta1,'precio':consulta2, 'id':consulta3}
    #precio= consulta["precio"]
    #print (categoria)
    longitud=[]
    for i in range(len(categoria["nombre"])):
        longitud.append(i)

    #print(categoria)
    #categoria=consulta["precio"]
    
    producto=[]
    cantidad=[]
    longitud_1=[]
    compra={'producto':producto,'cantidad':cantidad}
    
    if request.method=='POST':
        dat = request.form 
        for key,value in dat.items():
            #print(key," : ", value)
            if value !='0':
                producto.append(key)
                cantidad.append(value)
        
        
        print(compra)
        consulta1_1 =[]
        consulta2_1 =[]  
        consulta3_1 =[]
        consulta4_1 =[]
        
        for i in range(len(compra["producto"])):
            for datos in conexion.sentenciaCompuesta(" SELECT  pr.n_nomproducto, i.v_precio_unidad, i.K_PRODUCTO FROM PAIS p, REGION r, PRODUCTO pr, INVENTARIO i WHERE UPPER(p.n_nombre_pais)='COLOMBIA' AND p.k_pais=r.K_pais AND UPPER(r.n_nombre_region)='CARIBE' AND i.k_pais=r.K_pais AND i.k_region=r.k_region AND i.k_producto=pr.k_producto AND i.k_producto='"+ str(compra['producto'][i]) + "' order by pr.n_nomproducto asc"):
                consulta1_1.append(datos[0])
                consulta2_1.append(datos[1])
                consulta3_1.append(datos[2])
        print(consulta1_1)     
        
        
        for i in range(len(compra["producto"])):
            longitud_1.append(i)
            consulta4_1.append(int(cantidad[i])*int(consulta2_1[i]))
        
        dict['nombre']= consulta1_1
        dict['precio']= consulta2_1
        dict['id']= consulta3_1
        dict['total']= consulta4_1
        dict['longitud_1']=longitud_1
        dict['longitud']=longitud
        dict['compra']=compra
        categoria_1= {'nombre':consulta1_1,'precio':consulta2_1, 'id':consulta3_1,'total':consulta4_1}
        dict['categoria_1']= categoria_1
        print(categoria_1)
        print(longitud_1)
        #consulta4_1.sum()      
        subtotal= sum(consulta4_1)
        dict['subtotal']=subtotal
        total = (subtotal*0.19)+subtotal
        dict['total']=total
        return render_template('shopcart2.html',categoria_1=categoria_1,longitud_1=longitud_1,compra=compra,subtotal=subtotal, total=total)
        
    else:
        return render_template('shopcart.html',categoria=categoria,longitud=longitud)
    #return ?
    '''
    return render_template('shopcart.html',categoria=categoria,longitud=longitud)
    '''

# @shopCart.route("/go-to-pay", methods=["GET"])
# def show_product():
#     return render_template('pay.html',data=getUserAndPayMethod())

# @shopCart.route("/add-product-by-id-<int:product_id>", methods=["GET"])
# def add_product_to_cart(product_id):
#     products = getProductByID(product_id)
#     try:
#         with open('shop_cart.txt') as json_file:
#             products["data"] += json.load(json_file)
#     except error:
#         print(error) 
#     with open('shop_cart.txt', 'w') as outfile:
#         json.dump(products, outfile) 
#     return render_template('shopcart.html', products=products)  

######################## Metodos para las rutas de categories ######################################

#PARA ENVIAR EL RESPONSE_BODY COMPLETO YO TOME LA PALABRA INFO, PODRIA SER UNA BUENA CONVENCION
#PARA CUANDO ALGUIEN REESCRIBA ALGO NO SE DAÑE LO DEL OTRO
@categories.route("/<string:name_category>", methods=["GET"])
def show_categories(name_category):
    if(name_category == "Todas"):
        return render_template('categories.html', info=getProductsOfAllCategory())
    else:
        return render_template('categories.html', info=getProductsOfDeterminateCategory(name_category))
######################## Metodos para las rutas del register ##########################################

@register.route("/", methods=["GET","POST"])
def show_product():
    conexion = connect()

    if request.method=='POST':
        dat = request.form
        print('datos pago:', dat)
        clave=[]
        valor=[]
        for key,value in dat.items():
            #print(key," : ", value)
            clave.append(key)
            valor.append(value)
        long_form=[]
        for i in range(len(clave)):
            long_form.append(i)
        dict['form']={"clave":clave, "valor":valor}
        dict['long_form']=long_form
        print('diccionario:',dict['long_form'],dict['form'])
        print('User', dict['form']['valor'][11])

        USER_DATA["k_identificacion"]=1111111112
        conexion.sentenciaSimple("Insert into Usuario(K_TIPOID,K_IDENTIFICACION,N_NOMBRE,N_APELLIDO,N_CORREOE,N_DIRECCION,Q_TELEFONO,N_USUARIO) values ('"+str(dict['form']['valor'][3])+"','"+str(dict['form']['valor'][2])+"','"+str(dict['form']['valor'][0])+"', '"+str(dict['form']['valor'][1])+"','"+str(dict['form']['valor'][4])+"','"+str(dict['form']['valor'][5])+"','"+str(dict['form']['valor'][6])+"', '"+str(dict['form']['valor'][11])+"')")
        conexion.sentenciaSimple("Insert into REPRESENTANTE(K_TIPOID,K_IDENTIFICACION,I_GENERO,F_NACIMIENTO,F_CONTRATO,K_PAIS,K_REGION,Q_CALIFICACION,I_ESTADO,K_TIPOID_SUP,K_IDENTIFICACION_SUP) values ('"+str(dict['form']['valor'][3])+"','"+str(dict['form']['valor'][2])+"','"+str(dict['form']['valor'][7])+"',to_date('"+str(dict['form']['valor'][9])+"','DD/MM/RRRR'),sysdate,'1','"+str(dict['form']['valor'][8])+"',NULL,'A','CC','"+str(USER_DATA["k_identificacion"])+"')")
        conexion.sentenciaSimple("CREATE USER "+str(dict['form']['valor'][11])+" IDENTIFIED BY 1234 DEFAULT TABLESPACE natameCli TEMPORARY TABLESPACE natameCliTMP QUOTA 2M ON natamedef PASSWORD EXPIRE")
        conexion.sentenciaSimple("GRANT rol_representante TO "+str(dict['form']['valor'][11]))
        conexion.commint()
        
        return render_template('home.html')
    #Arreglar como se guardan los valores, crear una lista de las palabras y hacer una longitud para agregar
    return render_template('register.html')

@register_cliente.route("/", methods=["GET","POST"])
def show_product():
    conexion = connect()

    if request.method=='POST':
        dat = request.form
        print('datos pago:', dat)
        clave=[]
        valor=[]
        for key,value in dat.items():
            #print(key," : ", value)
            clave.append(key)
            valor.append(value)
        long_form_cliente=[]
        for i in range(len(clave)):
            long_form_cliente.append(i)
        dict['form_cliente']={"clave":clave, "valor":valor}
        dict['long_form_cliente']=long_form_cliente
        print('diccionario:',dict['long_form_cliente'],dict['form_cliente'])
        print('User', dict['form_cliente']['valor'][8])

        
        conexion.sentenciaSimple("Insert into Usuario(K_TIPOID,K_IDENTIFICACION,N_NOMBRE,N_APELLIDO,N_CORREOE,N_DIRECCION,Q_TELEFONO,N_USUARIO) values ('"+str(dict['form_cliente']['valor'][3])+"','"+str(dict['form_cliente']['valor'][2])+"','"+str(dict['form_cliente']['valor'][0])+"', '"+str(dict['form_cliente']['valor'][1])+"','"+str(dict['form_cliente']['valor'][4])+"','"+str(dict['form_cliente']['valor'][5])+"','"+str(dict['form_cliente']['valor'][6])+"', '"+str(dict['form_cliente']['valor'][8])+"')")
        conexion.sentenciaSimple("Insert into cliente(K_TIPOID,K_IDENTIFICACION,N_CIUDAD) values ('"+str(dict['form_cliente']['valor'][3])+"','"+str(dict['form_cliente']['valor'][2])+"','"+str(dict['form_cliente']['valor'][7])+"')")
        conexion.sentenciaSimple("CREATE USER "+str(dict['form_cliente']['valor'][8])+" IDENTIFIED BY 1234 DEFAULT TABLESPACE natameCli TEMPORARY TABLESPACE natameCliTMP QUOTA 2M ON natamedef PASSWORD EXPIRE")
        conexion.sentenciaSimple("GRANT rol_cliente TO "+str(dict['form_cliente']['valor'][8]))
        conexion.commint()
        
        return render_template('home.html')
    #Arreglar como se guardan los valores, crear una lista de las palabras y hacer una longitud para agregar
    return render_template('register_cliente.html')


    ######################## Metodos para las rutas del login ##########################################

@login.route('/', methods=['GET'])
def login_get():
    return render_template('login.html')

USER_DATA = {"k_tipoid":"","k_identificacion":-1,"n_usuario":"","k_region":-1,"rol":""}

@login.route("/", methods=["POST"])
def login_post():
    usuario = request.form.get('email')
    password = request.form.get('pass')
    
    if usuario == "" or password == "":
        flash('Please check your login details and try again.')
        return redirect(url_for('login.show_product')) # if the user doesn't exist or password is wrong, reload the page
    #user = get_user(usuario)
    global conexion
    conexion = connect(usuario,password)
    connected = conexion.getConnectionState()
    if not connected:
        flash('Please check your login details and try again.')
        return redirect(url_for('login.show_product')) # if the user doesn't exist or password is wrong, reload the page
    #login_user(user, remember=False)
    user_role = ""
    query_rol = "select distinct granted_role from USER_ROLE_PRIVS where upper(username)=upper('"+usuario+"')"
    user_role = conexion.sentenciaCompuesta(query_rol)[0][0]
    query = """select u.k_tipoid, u.k_identificacion, r.k_region 
        from natame.representante_para_cliente r, natame.representante_cliente rp, natame.cliente c, natame.usuario u 
        where r.k_identificacion=rp.k_identificacion_rep 
        and c.k_identificacion = rp.k_identificacion_cli 
        and c.k_tipoid = rp.k_tipoid_cli
        and rp.f_fin_rep is null 
        and c.k_identificacion = u.k_identificacion 
        and c.k_tipoid = u.k_tipoid 
        and u.n_usuario='""" + usuario + "'"
    datos_cookie=[]
    for dato in conexion.sentenciaCompuesta(query):
        datos_cookie.append(dato[0])
        datos_cookie.append(dato[1])
        datos_cookie.append(dato[2])
    USER_DATA["k_tipoid"] = datos_cookie[0]
    USER_DATA["k_identificacion"] = datos_cookie[1]
    USER_DATA["n_usuario"] = usuario
    USER_DATA["rol"]= user_role
    if len(datos_cookie)!=0:
        USER_DATA["k_region"] = datos_cookie[2]
    print(USER_DATA)
    return redirect(url_for('home.show_product'))


#End Login

#Errores

@home.errorhandler(403)
def forbidden(error):
    return render_template('403.html'),403

@stadistics.route('/sales_by_region', methods=['GET'])
def show_sales_by_region():
    return render_template('stadistics.html', info=getSalesByAllRegions())

@stadistics.route('/products_best_seller', methods=['GET'])
def show_products_best_seller():
    return render_template('stadistics2.html', info=getBestSellingProductsByRegion())

@users.route('/', methods=['GET'])
def view_users():
    return "Hola"

@users.route('/view_my_clients', methods=['GET'])
def view_clients():
    return render_template('clients.html')

@users.route('/view_my_representants', methods=['GET'])
def view_representant():
    return render_template('representant.html')
    