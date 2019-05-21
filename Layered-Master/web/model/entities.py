from sqlalchemy import Column, Integer, String, Sequence, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import connector

class User(connector.Manager.Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, Sequence('usuarios_id_seq'), primary_key=True)
    codigo = Column(Integer(10))
    nombre = Column(String(50))
    apellido = Column(String(12))
    password = Column(String(120))
