from flask import Flask

app = Flask(__name__)


# blueprint for auth routes in our app
from user import user as user_blueprint
app.register_blueprint(user_blueprint)

# blueprint for non-auth parts of app
from main import main as main_blueprint
app.register_blueprint(main_blueprint)

