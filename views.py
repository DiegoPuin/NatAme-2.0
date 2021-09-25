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

@home.route("/", methods=["GET"])
def show_home():
    return render_template('home.html')

@shopBag.route("/", methods=["GET"])
def show_product():
    return render_template('shopbag.html')



######################## Metodos para las rutas de shopcart ######################################

@shopCart.route("/", methods=["GET","POST"])
def show_products_in_cart():
    categoria= carrito()
    #print (categoria)
    longitud = longitud_cat(categoria)
    #print(longitud)
    if request.method=='POST':
        compra = compra_1(request)
        #print(compra)
        categoria1 = categoria_1(compra)
        print('categoria1',categoria1)
        #longitud1= longitud_1(compra,categoria1)
        #print(longitud1)
        
        categoria_2 ={'nombre':categoria1['categoria_1']['nombre'],'precio':categoria1['categoria_1']['precio'],'id':categoria1['categoria_1']['id'],'total':categoria1['categoria_1']['total']}
        longitud_2 ={'longitud_1':categoria1['longitud_1']}
        print(categoria_2)
        print(longitud_2)
        

        
        return render_template('shopcart2.html',categoria_1=categoria_2,longitud_1=longitud_2,compra=compra)
    else:
        return render_template('shopcart.html',categoria=categoria,longitud=longitud)
       
    '''
        

    
    return render_template('shopcart.html')

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
