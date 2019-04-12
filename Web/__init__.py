import os

from flask import Flask, redirect,url_for
from flask_qrcode import QRcode

def create_app(test_config = None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY = 'Dont-Steal-IT',
        DATABASE = os.path.join(app.instance_path, 'Web.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py',silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    @app.route('/')
    def hello():
            auth.logout()
            return redirect(url_for('auth.login'))

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import warehouse
    app.register_blueprint(warehouse.bp)
    app.add_url_rule('/',endpoint='index')

    return app