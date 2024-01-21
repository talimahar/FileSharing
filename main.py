# main.py
from flask import Flask
from config import Config
from src.auth.controllers import auth_blueprint
from src.user_mgmt.controllers import user_mgmt_blueprint
from src.auth.models import db
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config.from_object(Config)

# Initialize the Flask-JWT-Extended extension after creating the app
jwt = JWTManager(app)

# Initialize the database
db.init_app(app)
with app.app_context():
    db.create_all()

# Register blueprints
app.register_blueprint(auth_blueprint, url_prefix='/api')
app.register_blueprint(user_mgmt_blueprint, url_prefix='/api')

if __name__ == '__main__':
    app.run()
