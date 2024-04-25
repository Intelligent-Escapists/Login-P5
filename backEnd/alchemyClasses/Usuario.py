from sqlalchemy import Column, Integer, String
from alchemyClasses import db

class Usuario(db.Model):
    __tablename__ = 'usuario'
    id_usuario = Column(Integer, primary_key=True)
    correo = Column(String(345),unique=True)
    password = Column(String(200))

    def __init__(self, correo, password):
        self.correo = correo
        self.password = password
