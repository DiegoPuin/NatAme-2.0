from flask import Flask
from conf.config import DevelopmentConfig

#Login
#from flask_login import LoginManager
#login_manager = LoginManager()
#/Login

def create_app(config=DevelopmentConfig):
    app = Flask(__name__, static_url_path="/static", static_folder='static')
    app.config.from_object(config)
    #login_manager.login_view = "login_get"
    #login_manager.init_app(app)
    from views import home, shopCart, shopBag, categories, login, register #Movido para evitar importaciones circulares
    ACTIVE_ENDPOINTS = [('/home', home), ('/shopcart', shopCart), ("/shopbag", shopBag), ("/categories", categories), ("/login", login), 
    ("/register", register)] #Movido para evitar importaciones circulares
    for url, blueprint in ACTIVE_ENDPOINTS:
        app.register_blueprint(blueprint, url_prefix=url)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run()
