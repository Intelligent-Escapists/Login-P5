from flask import Flask, request, jsonify
from flask_cors import CORS
from config import Applicationconfig
from alchemyClasses import db
from alchemyClasses.Usuario import Usuario

from controllers.usuarioController import usuario_blueprint

app = Flask(__name__)
app.config.from_object(Applicationconfig)
CORS(app, supports_credentials=True)
db.init_app(app)
app.register_blueprint(usuario_blueprint)


if __name__ == '__main__':
    app.run(debug=True)