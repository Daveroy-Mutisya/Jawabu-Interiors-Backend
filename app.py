from flask import Flask, request, jsonify, Blueprint, make_response
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity, create_refresh_token
from flask_mail import Mail, Message
from flask_bcrypt import Bcrypt
import os
from flask_restful import Api, Resource
from models import db, Projects, Blogs, Users, Status
from flask_migrate import Migrate
from flask_cors import CORS, cross_origin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import timedelta
import logging
import re
from datetime import datetime


profile_bp = Blueprint('profile', __name__)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///JW.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')  
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=120) 
app.config['MAIL_SERVER'] = 'smtp.gmail.com' 
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
INVITE_REGISTER_TOKEN = os.getenv('INVITE_REGISTER_TOKEN')

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
    return "Welcome to Jawabu Interiors Backend"


# ROUTE FOR CONTACT FORM

class Contact(Resource):
    @cross_origin
    def post(self):
        data = request.get_json()
        email = data.get_json()
        name = data.get_json()
        message = data.get_json()
        subject = data.get_json()
        

############ LOGIN ROUTE ################################################################################################
def create_jwt_token(user):
    additional_claims = {
        'id': user.id,
        'super_user': user.super_user
    }
    access_token = create_access_token(identity=user.email, additional_claims=additional_claims)
    return access_token

def create_token_for_user(user):
    identity = {
        'id': user.id,
        'super_user': user.super_user, 
    }
    access_token = create_access_token(identity=identity)
    return access_token

class Login(Resource):
    def post(self):
        data = request.get_json()
        if not data:
            return {"error": "Missing data in request"}, 400

        email = data.get('email')
        password = data.get('password')
        
        user = Users.query.filter_by(email=email).first()
        
        if not user:
            return {"error": "User does not exist"}, 401

        logging.debug(f"User found: {user}")
        logging.debug(f"Stored hashed password: {user._password}")

        if not user.check_password(password):
            logging.debug(f"Password check failed for user: {user.email}")
            return {"error": "Incorrect password"}, 401

        access_token = create_token_for_user(user)
        refresh_token = create_refresh_token(identity={'id': user.id, 'super_user': user.super_user, 'email': user.email})
        return {"access_token": access_token, "refresh_token": refresh_token}, 200

api.add_resource(Login, '/login')

#################################ROUTE FOR TESTING PASSWORDS#######################################################################
@app.route('/test-password', methods=['POST'])
def test_password():
    data = request.get_json()
    password = data.get('password')
    
    hashed_password = generate_password_hash(password)
    logging.debug(f"Generated hash: {hashed_password}")
    
    is_password_correct = check_password_hash(hashed_password, password)
    logging.debug(f"Password check result: {is_password_correct}")
    
    return jsonify({
        'password': password,
        'hashed_password': hashed_password,
        'is_password_correct': is_password_correct
    }), 200

#################### ROUTE FOR TokenRefresh (WORKS) IS FOR EVERYONE #####################################################
class TokenRefresh(Resource):
    @cross_origin() 
    @jwt_required(refresh=True)
    def post(self):
        try:
            current_user = get_jwt_identity()
            access_token = create_access_token(identity=current_user)
            return {'access_token': access_token}, 200
        except Exception as e:
            return jsonify(error=str(e)), 500

api.add_resource(TokenRefresh, '/refresh-token')

##########################ROUTE FOR PROJECTS ##############################################################################################
class Project(Resource):
    @cross_origin()
    def get(self, id=None):
        if id:
            # Fetch a single project by ID
            project = Projects.query.get(id)
            if not project:
                return {"error": "Project not found"}, 404
            return jsonify(project.serialize()), 200

        # Fetch all projects
        projects = Projects.query.all()
        serialized_projects = [project.serialize() for project in projects]
        return jsonify(serialized_projects), 200

    @cross_origin()
    @jwt_required()
    def post(self):
        data = request.get_json()
        if not data:
            return {"error": "Missing data in request"}, 400

        current_user = get_jwt_identity()
        logging.debug(f"Current user from JWT: {current_user}")
        user_email = current_user.get('email')
        if not user_email:
            return {"error": "User email not found in token"}, 400
        
        user = Users.query.filter_by(email=user_email).first()
        if not user:
            return {"error": "User not found"}, 404

        project = Projects(
            title=data.get('title'),
            project_name=data.get('project_name'),
            image=data.get('image'),
            description=data.get('description'),
            location=data.get('location'),
            date=data.get('date'),
            user_id=user.id
        )

        db.session.add(project)
        db.session.commit()

        return project.serialize(), 201

    @cross_origin()
    @jwt_required()
    def put(self, id):
        data = request.get_json()
        if not data:
            return {"error": "Missing data in request"}, 400

        project = Projects.query.get(id)
        if not project:
            return {"error": "Project not found"}, 404

        project.title = data.get('title', project.title)
        project.project_name = data.get('project_name', project.project_name)
        project.image = data.get('image', project.image)
        project.description = data.get('description', project.description)
        project.location = data.get('location', project.location)
        project.date = data.get('date', project.date)

        db.session.commit()

        return project.serialize(), 200

    @cross_origin()
    @jwt_required()
    def delete(self, id):
        project = Projects.query.get(id)
        if not project:
            return {"error": "Project not found"}, 404

        db.session.delete(project)
        db.session.commit()

        return {"message": "Project deleted"}, 200

# Add the resource to the API
api.add_resource(Project, '/projects', '/projects/<int:id>')

############## ROUTE FOR BLOGS ############################################################?
class Blog(Resource):
    @cross_origin()
    def get(self, id=None):
        if id:
            # Fetch a single blog by ID
            blog = Blogs.query.get(id)
            if not blog:
                return {"error": "Blog not found"}, 404
            return jsonify(blog.serialize()), 200

        # Fetch all blogs
        blogs = Blogs.query.all()
        serialized_blogs = [blog.serialize() for blog in blogs]
        return jsonify(serialized_blogs), 200

    @cross_origin()
    @jwt_required()
    def post(self):
        data = request.get_json()
        if not data:
            return {"error": "Missing data in request"}, 400

        current_user = get_jwt_identity()
        logging.debug(f"Current user from JWT: {current_user}")
        user_email = current_user.get('email')
        if not user_email:
            return {"error": "User email not found in token"}, 400
        
        user = Users.query.filter_by(email=user_email).first()
        if not user:
            return {"error": "User not found"}, 404

        blog = Blogs(
            title=data.get('title'),
            content=data.get('content'),
            image=data.get('image'),
            author_id=user.id
        )

        db.session.add(blog)
        db.session.commit()

        return blog.serialize(), 201

    @cross_origin()
    @jwt_required()
    def put(self, id):
        data = request.get_json()
        if not data:
            return {"error": "Missing data in request"}, 400

        blog = Blogs.query.get(id)
        if not blog:
            return {"error": "Blog not found"}, 404

        blog.title = data.get('title', blog.title)
        blog.content = data.get('content', blog.content)
        blog.image = data.get('image', blog.image)

        db.session.commit()

        return blog.serialize(), 200

    @cross_origin()
    @jwt_required()
    def delete(self, id):
        blog = Blogs.query.get(id)
        if not blog:
            return {"error": "Blog not found"}, 404

        db.session.delete(blog)
        db.session.commit()

        return {"message": "Blog deleted"}, 200

# Add the resource to the API
api.add_resource(Blog, '/blogs', '/blogs/<int:id>')

#############ROUTES FOR FETCHING USERS#####################################################
class User(Resource):
    @cross_origin()
    def get(self, id=None):
        if id:
            user = Users.query.get(id)
            if not user:
                return {"error": "User not found"}, 404
            return jsonify(user.serialize()), 200

        users = Users.query.all()
        serialized_users = [user.serialize() for user in users]
        return jsonify(serialized_users), 200

    @cross_origin()
    @jwt_required()
    def post(self):
        data = request.get_json()
        if not data:
            return {"error": "Missing data in request"}, 400

        # Validate email
        email = data.get('email')
        assert '@' in email, "Email must contain '@'"
        assert re.match(r"[^@]+@[^@]+\.[^@]+", email), "Invalid email format"

        # Hash password
        password = data.get('password')
        hashed_password = generate_password_hash(password)

        user = Users(
            name=data.get('name'),
            username=data.get('username'),
            email=email,
            _password=hashed_password,
            image=data.get('image'),
            department=data.get('department'),
            status=Status.ONLINE,  # Default status
            bio=data.get('bio'),
            super_user=data.get('super_user', False),
            created_at=datetime.utcnow()
        )

        db.session.add(user)
        db.session.commit()

        return user.serialize(), 201

    @cross_origin()
    @jwt_required()
    def put(self, id):
        data = request.get_json()
        if not data:
            return {"error": "Missing data in request"}, 400

        user = Users.query.get(id)
        if not user:
            return {"error": "User not found"}, 404

        user.name = data.get('name', user.name)
        user.username = data.get('username', user.username)
        user.email = data.get('email', user.email)
        if 'password' in data:
            user._password = generate_password_hash(data['password'])
        user.image = data.get('image', user.image)
        user.department = data.get('department', user.department)
        user.status = data.get('status', user.status)
        user.bio = data.get('bio', user.bio)
        user.super_user = data.get('super_user', user.super_user)

        db.session.commit()

        return user.serialize(), 200

    @cross_origin()
    @jwt_required()
    def delete(self, id):
        user = Users.query.get(id)
        if not user:
            return {"error": "User not found"}, 404

        db.session.delete(user)
        db.session.commit()

        return {"message": "User deleted"}, 200

api.add_resource(User, '/users', '/users/<int:id>')



if __name__ == '__main__':
    app.run(debug=True)
