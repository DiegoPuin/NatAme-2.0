""" from http import HTTPStatus
from flask_login import UserMixin
from flask import Blueprint, Response, request, render_template, url_for
from connect_db import connect 
from werkzeug.security import generate_password_hash, check_password_hash
from app import login_manager

@login_manager.user_loader
def load_user(usuario):
    return get_user(usuario)

def get_user(usuario):
    conn = connect()
    query = select * from usuario where N_USUARIO = (:1)
    username = usuario
    datos_de_usuario = conn.sentenciaPreparada(query,username)
    conn.close()
    if len(datos_de_usuario)>0:
        result = User(datos_de_usuario[0])
        return result
    else:
        return None

class User(UserMixin):
    def __init__(self,K_TIPOID, K_IDENTIFICACION, N_NOMBRE, N_APELLIDO, N_CORREOE, N_DIRECCION, Q_TELEFONO, K_TIPOID_USUP, K_IDENTIFICACION_USUP,N_USUARIO,N_CONTRASENA):
        self.id = K_TIPOID
        self.K_IDENTIFICACION= K_IDENTIFICACION
        self.N_NOMBRE= N_NOMBRE
        self.N_APELLIDO= N_APELLIDO
        self.N_CORREOE= N_CORREOE
        self.N_DIRECCION= N_DIRECCION
        self.Q_TELEFONO= Q_TELEFONO
        self.K_TIPOID_USUP= K_TIPOID_USUP
        self.K_IDENTIFICACION_USUP= K_IDENTIFICACION_USUP
        self.N_USUARIO= N_USUARIO
        self.N_CONTRASENA=N_CONTRASENA

    def __init__(self,datos):
        self.id = datos[0]
        self.K_IDENTIFICACION= datos[1]
        self.N_NOMBRE= datos[2]
        self.N_APELLIDO= datos[3]
        self.N_CORREOE= datos[4]
        self.N_DIRECCION= datos[5]
        self.Q_TELEFONO= datos[6]
        self.K_TIPOID_USUP= datos[7]
        self.K_IDENTIFICACION_USUP= datos[8]
        self.N_USUARIO= datos[9]
        self.N_CONTRASENA=datos[10]

    def set_password(self, password):
        self.N_CONTRASENA = generate_password_hash(password)

    def check_password(self, password):
        return self.N_CONTRASENA == password

    def __repr__(self):
        return '<User {}>'.format(self.N_USUARIO) """