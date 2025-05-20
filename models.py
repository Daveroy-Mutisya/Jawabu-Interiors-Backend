# models.py 
from sqlalchemy_serializer import SerializerMixin
from enum import Enum
from sqlalchemy.orm import validates
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import re

db = SQLAlchemy()

# Enumeration for Status
class Status(Enum):
    OFFLINE = 'Offline'
    ONLINE = 'Online'
    ON_LEAVE = 'On Leave'

# Users Model
class Users(db.Model, SerializerMixin):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    _password = db.Column('password', db.String(100), nullable=False)  # Use _password to store the hashed password
    image = db.Column(db.String(100), nullable=True)
    department = db.Column(db.String(100), nullable=True)
    status = db.Column(db.Enum(Status), default=Status.ONLINE, nullable=True)
    bio = db.Column(db.String(500), nullable=True)
    super_user = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    projects = db.relationship('Projects', backref='owner', lazy=True)
    blog_posts = db.relationship('Blogs', backref='author', lazy=True)

    @validates('email')
    def validate_email(self, key, email):
        assert '@' in email, "Email must contain '@'"
        assert re.match(r"[^@]+@[^@]+\.[^@]+", email), "Invalid email format"
        return email

    def set_password(self, password):
        self._password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self._password, password)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'username': self.username,
            'email': self.email,
            'image': self.image,
            'department': self.department,
            'status': self.status.value,  # Convert Enum to string
            'bio': self.bio,
            'super_user': self.super_user,
            'created_at': self.created_at
        }

    def __repr__(self):
        return f"Users <{self.id}, {self.username}, {self.name}, {self.image}, {self.department}, {self.email}, {self.bio}, {self.super_user}>"

# Projects Model
class Projects(db.Model, SerializerMixin):
    __tablename__ = 'Projects'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=True)
    project_name = db.Column(db.String, nullable=True)
    before_image = db.Column(db.String, nullable=True)
    after_image = db.Column(db.String, nullable=True)
    description = db.Column(db.String, nullable=True)
    location = db.Column(db.String, nullable=True)
    date = db.Column(db.String, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.id'), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'project_name': self.project_name,
            'before_image': self.before_image,
            'after_image': self.after_image,
            'description': self.description,
            'location': self.location,
            'date': self.date,
            'user_id': self.user_id
        }

    def __repr__(self):
        return f"Projects <{self.id}, {self.title}, {self.project_name}, {self.before_image},{self.after_image}, {self.description}, {self.location}, {self.date}, {self.user_id}>"

# Blogs Model
class Blogs(db.Model, SerializerMixin):
    __tablename__ = 'BlogPost'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.Text, nullable=False)
    image = db.Column(db.String, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    author_id = db.Column(db.Integer, db.ForeignKey('Users.id'), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'image': self.image,
            'created_at': self.created_at,
            'author_id': self.author_id
        }

    def __repr__(self):
        return f"Blogs <{self.id}, {self.title}, {self.content}, {self.image}, {self.created_at}, {self.author_id}>"

# Contact Model
class Contact(db.Model, SerializerMixin):
    __tablename__ = 'ContactForm'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    surname = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    phone_number = db.Column(db.String, nullable=False)
    project_type = db.Column(db.String, nullable=False)
    description = db.Column(db.Text, nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'surname': self.surname,
            'email': self.email,
            'phone_number': self.phone_number,
            'project_type': self.project_type,
            'description': self.description,
        }

    def __repr__(self):
        return f"Contact <{self.id}, {self.first_name}, {self.surname}, {self.email}, {self.phone_number}, {self.project_type}, {self.description}>"



