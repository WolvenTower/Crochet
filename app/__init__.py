from flask import Flask

def create_app():
    app = Flask(__name__,template_folder='./app/templates',static_folder='./static')

    # Configuration settings
    app.config['SECRET_KEY'] = 'your_secret_key'

    # Register blueprints
    from . import routes
    app.register_blueprint(routes.bp)

    return app
