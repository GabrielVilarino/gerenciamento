# models.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuario"
    __table_args__ = {"schema": "gerenciamento"}

    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario = Column(String(30), nullable=False)
    senha = Column(String(30), nullable=False)
    tipo_usuario = Column(String(30), nullable=False)
