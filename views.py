from http import HTTPStatus
from flask import Blueprint, Response, request, render_template, url_for, redirect, flash
from werkzeug.wrappers import response
import json
#from models import User,get_user
#from app import login_manager
#from flask_login import current_user, login_user, login_required
from querys import *

home = Blueprint("home", __name__, url_prefix="/home")
shopCart = Blueprint("shopcart", __name__, url_prefix="/shopcart")
shopBag = Blueprint("shopbag", __name__, url_prefix="/shopbag")
categories = Blueprint("categories", __name__, url_prefix="/categories")
login = Blueprint("login", __name__, url_prefix="/login")
register = Blueprint("register", __name__, url_prefix="/register")
shopCart2 = Blueprint("shopcart2", __name__, url_prefix="/shopcart2")

dict={}

@home.route("/", methods=["GET"])
def show_home():
    return render_template('home.html')

@shopBag.route("/", methods=["GET"])
def show_product():
    return render_template('shopbag.html')



######################## Metodos para las rutas de shopcart ######################################


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

    print(categoria, longitud)
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
        categoria_1= {'nombre':consulta1_1,'precio':consulta2_1, 'id':consulta3_1,'total':consulta4_1}
        print(categoria_1)
        print(longitud_1)
        #consulta4_1.sum()      
        subtotal= sum(consulta4_1)
        
        return render_template('shopcart2.html',categoria_1=categoria_1,longitud_1=longitud_1,compra=compra,subtotal=subtotal)
        
    else:
        return render_template('shopcart.html',categoria=categoria,longitud=longitud)
    #return ?
    '''
    return render_template('shopcart.html',categoria=categoria,longitud=longitud)
    '''
'''
@shopCart.route("/go-to-pay", methods=["GET"])
def show_product():
    return render_template('pay.html',data=getUserAndPayMethod())


@shopCart.route("/add-product-by-id-<int:product_id>", methods=["GET"])
def add_product_to_cart(product_id):
    products = getProductByID(product_id)
    """ try:
        with open('shop_cart.txt') as json_file:
            products["data"] += json.load(json_file)
    except error:
        print(error) """
    """ with open('shop_cart.txt', 'w') as outfile:
        json.dump(products, outfile) """
    return render_template('shopcart.html', products=products)  
'''
######################## Metodos para las rutas de categories ######################################

@categories.route("/", methods=["GET"])
def show_categories():
    return render_template('categories.html', products=getProductsWhitPrice()) 
     
######################## Metodos para las rutas del register ##########################################

@register.route("/", methods=["GET"])
def show_product():
    return render_template('register.html')

    ######################## Metodos para las rutas del login ##########################################

@login.route('/', methods=['GET'])
def login_get():
    return render_template('login.html')

""" @login.route('/?username=<string:user_name>&password=<string:passw>', methods=['GET'])
def login_get():
    return render_template('login.html')
     """

@login.route('/', methods=['POST'])
def login_post():
    print("Entra aca")
    usuario = request.form.get('username')
    password = request.form.get('password')
    
    """ user = get_user(usuario)
    if not user or not user.check_password(password):
        flash('Por favor revisa tus credenciales e intenta de nuevo.')
        return redirect(url_for('login.login_get')) 
    login_user(user, remember=False) """
    data = getAutentication(usuario, password)
    if data:
        return render_template('home.html')
    else:
        return data
