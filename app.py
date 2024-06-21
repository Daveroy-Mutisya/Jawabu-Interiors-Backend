from flask import Flask, request, jsonify, Blueprint, make_response
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity, create_refresh_token
from flask_mail import Mail, Message
from flask_bcrypt import Bcrypt
import os
from flask_restful import Api, Resource
from models import db
from flask_migrate import Migrate
from flask_cors import CORS, cross_origin
import models
from datetime import timedelta
import logging
from werkzeug.security import generate_password_hash, check_password_hash

profile_bp = Blueprint('profile', __name__)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///JawabuInteriors.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')  
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=120) 
app.config['MAIL_SERVER'] = 'smtp.gmail.com' 
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
INVITE_REGISTER_TOKEN = os.environ.get('INVITE_REGISTER_TOKEN')

# Initialize Flask extensions
db.init_app(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
mail = Mail(app)
api = Api(app)
migrate = Migrate(app, db)

# Configure CORS
CORS(app, resources={r"/*": {
    "origins": "*",
    "methods": ["GET", "POST", "PUT", "DELETE"],
    "allow_headers": ["Content-Type", "Authorization"],
    "supports_credentials": True
}})

logging.basicConfig(level=logging.DEBUG)

@app.route('/api/data', methods=["GET", "POST", "PUT", "DELETE"])
def handle_data():
    return 'This is some data from the API.'

####################### HOME BACKEND ROUTE ##############################################################
@app.route('/', methods=['GET'])
def home():
    return "Welcome to my Duka Backend"

############ LOGIN ROUTE ################################################################################################
# def create_jwt_token(user):
#     additional_claims = {
#         'id': user.id,
#         'role': user.role
#     }
#     access_token = create_access_token(identity=user.email, additional_claims=additional_claims)
#     return access_token

# def create_token_for_user(user):
#     identity = {
#         'id': user.id,
#         'role': user.role, 
#     }
#     access_token = create_access_token(identity=identity)
#     return access_token

# class Login(Resource):
#     def post(self):
#         data = request.get_json()
#         if not data:
#             return {"error": "Missing data in request"}, 400

#         email = data.get('email')
#         password = data.get('password')
        
#         # Check for the user in all the models
#         user = 5
        
#         if not user:
#             return {"error": "User does not exist"}, 401

#         # Debugging: Print user details and stored hashed password
#         logging.debug(f"User found: {user}")
#         logging.debug(f"Stored hashed password: {user._password}")

#         # Check password using model's method
#         if not user.check_password(password):
#             logging.debug(f"Password check failed for user: {user.email}")
#             return {"error": "Incorrect password"}, 401

#         access_token = create_token_for_user(user)
#         refresh_token = create_refresh_token(identity={'id': user.id, 'role': user.role, 'email': user.email})
#         return {"access_token": access_token, "refresh_token": refresh_token}, 200

# api.add_resource(Login, '/login')


# ROUTE FOR TESTING PASSWORDS
# @app.route('/test-password', methods=['POST'])
# def test_password():
#     data = request.get_json()
#     password = data.get('password')
    
#     # Hash the password
#     hashed_password = generate_password_hash(password)
#     logging.debug(f"Generated hash: {hashed_password}")
    
#     # Check the password
#     is_password_correct = check_password_hash(hashed_password, password)
#     logging.debug(f"Password check result: {is_password_correct}")
    
#     return jsonify({
#         'password': password,
#         'hashed_password': hashed_password,
#         'is_password_correct': is_password_correct
#     }), 200


# #################### ROUTE FOR TokenRefresh (WORKS) IS FOR EVERYONE #####################################################
# class TokenRefresh(Resource):
#     @cross_origin() 
#     @jwt_required(refresh=True)
#     def post(self):
#         try:
#             current_user = get_jwt_identity()
#             access_token = create_access_token(identity=current_user)
#             return {'access_token': access_token}, 200
#         except Exception as e:
#             return jsonify(error=str(e)), 500

# api.add_resource(TokenRefresh, '/refresh-token')

if __name__ == '__main__':
    app.run(debug=True)
