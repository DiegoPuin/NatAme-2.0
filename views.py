from http import HTTPStatus
from flask import Blueprint, Response, request, render_template, url_for, redirect, flash
from werkzeug.wrappers import response
from connect_db import connect
from models import User,get_user
from app import login_manager
from flask_login import current_user, login_user, login_required
import sys

import pandas as pd

home = Blueprint("home", __name__, url_prefix="/home")
shopCart = Blueprint("shopcart", __name__, url_prefix="/shopcart")
shopBag = Blueprint("shopbag", __name__, url_prefix="/shopbag")
categories = Blueprint("categories", __name__, url_prefix="/categories")
login = Blueprint("login", __name__, url_prefix="/login")
register = Blueprint("register", __name__, url_prefix="/register")

RESPONSE_BODY = {"message": "", "data": [], "errors": [], "metadata": []}

@home.route("/", methods=["GET"])
def show_product():
    
    conexion = connect()
    for datos in conexion.sentenciaCompuesta("select N_NOMCATEGORIA from categoria where K_CATEGORIA_PERTENECE is null"):
        RESPONSE_BODY["data"] += datos
    conexion.close()
    categoria1=RESPONSE_BODY["data"][1]
    return render_template('home.html', categoria1=categoria1)

@shopBag.route("/", methods=["GET"])
def show_product():
    return render_template('shopbag.html')

@shopCart.route("/", methods=["GET"])
def show_product():
    conexion = connect()
    ejemplo = []
    for datos in conexion.sentenciaCompuesta("select N_NOMCATEGORIA from categoria where K_CATEGORIA_PERTENECE is null"):
        ejemplo["data"] += datos
        #pass
    categoria=ejemplo["data"]
    return render_template('shopcart.html',categoria=categoria)

@shopCart.route("/drop/<int:product_id>", methods=["GET"])
def delete_from_cart(product_id):
    pass

######################## Metodos para las rutas de categories ######################################

@categories.route("/", methods=["GET"])
def show_product():
    conexion = connect()
    for datos in conexion.sentenciaCompuesta("select N_NOMCATEGORIA from categoria"):
        RESPONSE_BODY["data"] += datos
    conexion.close()
    categorias = RESPONSE_BODY["data"]
    return render_template('categories.html', categorias=categorias)
     
######################## Metodos para las rutas del login ######################################

@register.route("/", methods=["GET"])
def show_product():
    return render_template('register.html')

def vaciar_RESPONSE():
    RESPONSE_BODY = {"message": "", "data": [], "errors": [], "metadata": []}

@login.route('/', methods=['GET'])
def login_get():
    return render_template('login.html')

@login.route('/', methods=['POST'])
def login_post():
    usuario = request.form.get('username')
    password = request.form.get('password')
    user = get_user(usuario)
    if not user or not user.check_password(password):
        flash('Por favor revisa tus credenciales e intenta de nuevo.')
        return redirect(url_for('login.login_get')) 
    login_user(user, remember=False)
    return redirect(url_for('home.show_product'))