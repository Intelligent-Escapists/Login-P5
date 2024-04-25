from flask import request, abort, session
from flask.json import jsonify
from cryptoUtils import CryptoUtils as crypto

from alchemyClasses.Usuario import Usuario
from alchemyClasses import db


def crear_usuario(correo,password):
    nuevo_usuario = Usuario(correo=correo, password=password)

    try:
        db.session.add(nuevo_usuario)
        db.session.commit()
    except Exception as e:
        abort(400, str(e))

    return nuevo_usuario

def buscar_usuario(correo, password):
    usuario = Usuario.query.filter_by(correo=correo).first()

    if usuario is None:
        return None

    if crypto.validate(password, usuario.password):
        return usuario

    return None
def buscar_usuario_por_id(id_usuario):
    return Usuario.query.filter_by(id_usuario=id_usuario).first()


def existe_usuario(correo):

    return Usuario.query.filter_by(correo=correo).first() is not None