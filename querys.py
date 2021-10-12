from os import error
from connect_db import connect

#RETORNAR EL RESPONSE BODY COMPLETO PARA ASI PODER SELECCIONAR LOS 
#DATOS QUE NECESITEMOS SIN INTERFERIR EN LO QUE HACE EL OTRO
RESPONSE_BODY = {"products": [], "categories": [], "current_category": "", "current_region": "Andina", "USER_LOCAL": "",
 "regions": [], "error": "", "stadistics": [], "cli_repre": ""}
LOCAL_USER_ID = -1

def getCategoriesNames(cant):
    vaciar_RESPONSE()
    conexion = connect()
    sql = "SELECT N_NOMCATEGORIA FROM categoria WHERE ROWNUM <= " + str(cant)
    for category in conexion.sentenciaCompuesta(sql):
        RESPONSE_BODY["data"] += {"name": category},
    conexion.close()
    return RESPONSE_BODY

#Cuando se trae un solo elemento en el SQL lo trae igual como
#una tupla asi que hay que decirle que en el response_body solo tenga
#en cuenta la posicion 0 para que la informacion se pase bien
def getAllCategoriesNames():
    conexion = connect()
    sql = "SELECT N_NOMCATEGORIA FROM categoria"
    for category in conexion.sentenciaCompuesta(sql):
        RESPONSE_BODY["categories"] += {"name": category[0]},
    conexion.close()
    return RESPONSE_BODY

def getRegionNames():
    vaciar_RESPONSE()
    conexion = connect()
    sql = "SELECT N_NOMBRE_REGION FROM region"
    for region in conexion.sentenciaCompuesta(sql):
        RESPONSE_BODY["data"] += {"name": region},
    conexion.close()
    return RESPONSE_BODY["data"]

def getProductsWhitPrice():
    conexion = connect()
    sql1 = "SELECT pr.k_producto, pr.n_nomproducto, i.v_precio_unidad FROM PAIS p, REGION r, PRODUCTO pr, INVENTARIO i WHERE UPPER(p.n_nombre_pais) " 
    sql2 = "=\'COLOMBIA\' AND p.k_pais=r.K_pais AND UPPER(r.n_nombre_region)= \'" + RESPONSE_BODY["current_region"].upper() + "\' AND i.k_pais=r.K_pais AND i.k_region=r.k_region" 
    sql3 = " AND i.k_producto=pr.k_producto"
    for id, name, price  in conexion.sentenciaCompuesta(sql1 + sql2 + sql3):
        RESPONSE_BODY["products"] += {"id": id, "name": name, "price": price},
    conexion.close()
    return RESPONSE_BODY

def getProductsWhitPriceOfOneCategory(category_name):
    conexion = connect()
    sql1 = "SELECT pr.k_producto, pr.n_nomproducto, i.v_precio_unidad FROM PAIS p, REGION r, PRODUCTO pr, INVENTARIO i, CATEGORIA c WHERE UPPER(p.n_nombre_pais) " 
    sql2 = "=\'COLOMBIA\' AND p.k_pais=r.K_pais AND UPPER(r.n_nombre_region)= \'" + RESPONSE_BODY["current_region"].upper() + "\' AND i.k_pais=r.K_pais AND i.k_region=r.k_region" 
    sql3 = " AND i.k_producto=pr.k_producto AND UPPER(c.n_nomcategoria) = \'" + category_name.upper() + "\' AND pr.k_categoria = c.k_categoria"  
    print(sql1 + sql2 + sql3)
    for id, name, price  in conexion.sentenciaCompuesta(sql1 + sql2 + sql3):
        RESPONSE_BODY["products"] += {"id": id, "name": name, "price": price},
    conexion.close()
    return RESPONSE_BODY

def getProductByID(id_product):
    RESPONSE_BODY = vaciar_RESPONSE()
    conexion = connect()
    sql1 = "SELECT pr.k_producto, pr.n_nomproducto, i.v_precio_unidad FROM PAIS p, REGION r, PRODUCTO pr, INVENTARIO i WHERE UPPER(p.n_nombre_pais) " 
    sql2 = "=\'COLOMBIA\' AND p.k_pais=r.K_pais AND UPPER(r.n_nombre_region)= \'" + RESPONSE_BODY["current_region"].upper() + "\' AND i.k_pais=r.K_pais AND i.k_region=r.k_region" 
    sql3 = " AND i.k_producto=pr.k_producto AND pr.k_producto=" + str(id_product)
    for id, name, price  in conexion.sentenciaCompuesta(sql1 + sql2 + sql3):
        RESPONSE_BODY["message"] = "SUCCESFULL"
        RESPONSE_BODY["data"] += {"id": id, "name": name, "price": price},
    conexion.close()
    return RESPONSE_BODY

def getAutentication(username, passw):
    vaciar_RESPONSE
    conexion = connect()
    try:
        #conexion.sentenciaSimple("connect " + username + "/" + passw)
        query = "select k_identificacion, n_nombre, n_usuario from usuario where N_USUARIO = '" + username + "'" 
        for id, name, user in conexion.sentenciaCompuesta(query):
            global LOCAL_USER_ID
            LOCAL_USER_ID = id
            RESPONSE_BODY["USER_LOCAL"] = id
            RESPONSE_BODY["data"] += {"id": id, "name": name, "user": user},
        conexion.close()
    except error:
        print("El usuario no se pudo conectar")
        print(error)
    return RESPONSE_BODY
    
def getUserAndPayMethod():
    conexion = connect()
    query = " select u.n_usuario, m.n_detalle_metodo_pago from metodo_de_pago m, cliente c, usuario u  where c.k_identificacion="
    "m.k_identificacion_cli and u.k_identificacion='" + RESPONSE_BODY["USER_LOCAL"] + "'and u.k_identificacion=c.k_identificacion"
    for name, pay in conexion.sentenciaCompuesta(query):
        RESPONSE_BODY["data"] += {"name": name, "pay_method": pay}
    conexion.close()
    return RESPONSE_BODY

def getProductsOfAllCategory():
    RESPONSE_BODY["current_category"] = "TODAS"
    getAllCategoriesNames()
    getProductsWhitPrice()
    return RESPONSE_BODY

def getProductsOfDeterminateCategory(category_name):
    RESPONSE_BODY["current_category"] = category_name.upper()
    getAllCategoriesNames()
    getProductsWhitPriceOfOneCategory(category_name)
    return RESPONSE_BODY

def getSalesByAllRegions():
    RESPONSE_BODY["stadistics"] = []
    conexion = connect()
    try:
        for region, sum in conexion.sentenciaFuncion("FU_REGIONAL_MAS_VENTAS"):
            RESPONSE_BODY["stadistics"] += {"region": region, "V_Total": sum},
        return RESPONSE_BODY
    except error:
        RESPONSE_BODY["error"] = error
        return RESPONSE_BODY

def getBestSellingProductsByRegion():
    RESPONSE_BODY["stadistics"] = []
    conexion = connect()
    try:
        for region, product, cantidad in conexion.sentenciaFuncion("FU_PROD_MAS_VENDIDO"):
            RESPONSE_BODY["stadistics"] += {"region": region, "product": product, "quantity": cantidad},
        return RESPONSE_BODY
    except error:
        RESPONSE_BODY["error"] = error
        return RESPONSE_BODY 

def getDataFromClientAndRepresentant(id_user):
    RESPONSE_BODY["cli_repre"] = []
    conexion = connect()
    try:
        for tipoid, identificacion, nombre, apellido, correo, direccion, telefono, ciudad, nombre_rep, apellido_rep in conexion.sentenciaFuncionParam("FU_DATOS_CLI_REP", [21111, 0, "null"]):
            RESPONSE_BODY["cli_repre"] += {"tipoid": tipoid, "id": identificacion, "name": nombre, "last_name": apellido, "email": correo, 
            "address": direccion, "phone": telefono, "city": ciudad, "rep_name": nombre_rep, "last_name_rep": apellido_rep},
        return RESPONSE_BODY
    except error:
        RESPONSE_BODY["error"] = error
        return RESPONSE_BODY


def vaciar_RESPONSE():
    global RESPONSE_BODY
    RESPONSE_BODY = {}
    return RESPONSE_BODY

def get_USER_LOCAL():
    return RESPONSE_BODY["USER_LOCAL"]

def carrito():
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
    return categoria

def longitud_cat (categoria):
    longitud=[]
    for i in range(len(categoria["nombre"])):
        longitud.append(i)
    return longitud

    #print(categoria)
    #categoria=consulta["precio"]
def compra_1(request):
    #conexion = connect()
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
    return compra        
        
''''''
#print(compra)
def categoria_1(compra):
    conexion = connect()
    longitud_1=[]
    consulta1_1 =[]
    consulta2_1 =[]  
    consulta3_1 =[]
    
    
    for i in range(len(compra["producto"])):
        for datos in conexion.sentenciaCompuesta(" SELECT  pr.n_nomproducto, i.v_precio_unidad, i.K_PRODUCTO FROM PAIS p, REGION r, PRODUCTO pr, INVENTARIO i WHERE UPPER(p.n_nombre_pais)='COLOMBIA' AND p.k_pais=r.K_pais AND UPPER(r.n_nombre_region)='CARIBE' AND i.k_pais=r.K_pais AND i.k_region=r.k_region AND i.k_producto=pr.k_producto AND i.k_producto='"+ str(compra['producto'][i]) + "' order by pr.n_nomproducto asc"):
            consulta1_1.append(datos[0])
            consulta2_1.append(datos[1])
            consulta3_1.append(datos[2])
    #print(consulta1_1)     
    #categoria_1= {'nombre':consulta1_1,'precio':consulta2_1, 'id':consulta3_1}
    
    #return categoria_1

#def longitud_1(compra,categoria_1):
    consulta4_1 =[]
    for i in range(len(compra["producto"])):
            longitud_1.append(i)
            consulta4_1.append(int(compra['cantidad'][i])*int(consulta2_1[i]))
        
    #categoria_1= {'nombre':categoria_1['nombre'],'precio':categoria_1['precio'], 'id':categoria_1['id'],'total':consulta4_1}
    categoria_1= {'nombre':consulta1_1,'precio':consulta2_1, 'id':consulta3_1,'total':consulta4_1}
    var ={'categoria_1':categoria_1, 'longitud_1':longitud_1}
    return var

    '''
print(categoria_1)
print(longitud_1)




return render_template('shopcart2.html',categoria_1=categoria_1,longitud_1=longitud_1,compra=compra)

else:
return render_template('shopcart.html',categoria=categoria,longitud=longitud)
'''