from flask import Flask, request, jsonify, url_for, Blueprint
import datetime
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token, get_jwt_identity 
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import db, User, Membership, Admin

api = Blueprint('api', __name__)

@api.route('/')
def index():
    return "Hola desde Burnoff Manager"

@api.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    full_name = data.get("full_name")
    phone = data.get("phone")
    membership_type = data.get("membership_type")
    membership_expire_date = data.get("membership_expire_date")

    if not full_name or not phone:
        return jsonify({'error': 'full_name and phone are required'}), 400

    if not membership_type or not membership_expire_date:
        user = User(full_name=full_name, phone=phone)
        user.save()
        return jsonify(user.to_dict()), 201
    
    membresia = Membership(type=membership_type, expires_at=membership_expire_date)
    membresia.save()

    user = User(full_name=full_name, phone=phone, membership_id=membresia.id)
    user.save()
    return jsonify(user.to_dict()), 201

@api.route('/registeradmins', methods=['POST'])
def create_admin():
    data= request.get_json()
    email = data.get("email")
    name = data.get("name")
    password = data.get("password")
    type = data.get("type")
    super_admin = data.get("super_admin")

    if not email:
        return jsonify({'msg':"Email is required"}),400

    if not name:
        return jsonify({'msg':"Name is required"}),400
    
    if not password:
        return jsonify({'msg':"Password is required"}),400
    
    if not type:
        return jsonify({'msg':"Type is required"}),400

    admin = Admin()
    admin.email = email
    admin.name = name
    admin.type=type
    admin.password = generate_password_hash(password)
    admin.super_admin=super_admin
    admin.save()
    
    if admin:
        return jsonify({'status':'success','message':'Admin successfully created'}),200
    
    return jsonify({'status':'error','message':'Error in admin creation, please try again'}),500

@api.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    if not email:
        return jsonify({'msg':'Username is required'}),400
    
    if not password:
        return jsonify({'msg':'Password is required'}),400
    
    admin = Admin.query.filter_by(email=email).first()

    if not admin:
        return jsonify({'msg':'Invalid credentials'}),401
    
    if not check_password_hash(admin.password, password):
        return jsonify ({'msg':'Invalid credentials'}), 401
    
    expire = datetime.timedelta(hours=2)
    token = create_access_token(identity=str(admin.id), expires_delta=expire)

    data = {
        "token": token,
        "admin": admin.to_dict()
    }

    return jsonify(data), 200