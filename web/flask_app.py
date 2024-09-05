from flask import Flask



def create_app():
    app = Flask(__name__)

    # blueprint for auth routes in our app
    from web.user import user as user_blueprint
    app.register_blueprint(user_blueprint)

    # blueprint for non-auth parts of app
    from web.main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app
