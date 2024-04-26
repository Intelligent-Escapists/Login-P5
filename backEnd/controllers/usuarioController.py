from flask import Blueprint, request, jsonify, session
from cryptoUtils import CryptoUtils as crypto
from hashlib import sha256


from model import modelUsuario as model

usuario_blueprint = Blueprint('usuario', __name__,url_prefix='/usuario')


@usuario_blueprint.route('/crear-usuario', methods=['POST'])
def crear_usuario():

    correo = request.json['correo']
    password = request.json['password']


    if model.existe_usuario(correo):
        return jsonify({"error": "El usuario ya existe"}), 409

    password_hashed = sha256(crypto.cipher(password)).hexdigest()

    nuevo_usuario = model.crear_usuario(correo, password_hashed)
    session['id_usuario'] = nuevo_usuario.id_usuario

    return jsonify({
        "id_usuario": nuevo_usuario.id_usuario,
        "correo": nuevo_usuario.correo,
        "password": nuevo_usuario.password
    })


@usuario_blueprint.route('/login-usuario', methods=['POST'])
def login_usuario():
    correo = request.json['correo']
    password = request.json['password']

    usuario = model.buscar_usuario(correo, password)

    if usuario is None:
        return jsonify({"error": "correo o contraseña incorrectos"}), 401
    
    session['id_usuario'] = usuario.id_usuario
    return jsonify({
            "id_usuario": usuario.id_usuario,
            "correo": usuario.correo,
            "password": usuario.password
        })
@usuario_blueprint.route('/logout-usuario', methods=['POST'])
def logout_usuario():
    session.pop('id_usuario', None)
    return "200"


@usuario_blueprint.route('/@usuario')
def get_usuario_autenticado():
    id_usuario = session.get('id_usuario')

    if not id_usuario:
        return jsonify({"error": "No autenticado"}), 401

    usuario = model.buscar_usuario_por_id(id_usuario)

    if usuario is None:
        return jsonify({"error": "Usuario no encontrado"}), 404
    
    return jsonify({
            "id_usuario": usuario.id_usuario,
            "correo": usuario.correo,
            "password": usuario.password
        })