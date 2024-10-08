from flask import Flask

def create_app():
    app = Flask(__name__)

    # You can configure the app here (optional)
    app.config['SECRET_KEY'] = 'your_secret_key'

    # Import and register blueprints (routes)
    from .routes import main_routes
    app.register_blueprint(main_routes)

    # You can also initialize other extensions here, e.g., database, login manager, etc.
    # from .extensions import db, login_manager
    # db.init_app(app)
    # login_manager.init_app(app)

    return app