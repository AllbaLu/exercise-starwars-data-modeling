import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

# el usuario debe tener planetas y personajes favoritos


class Usuario(Base):
    __tablename__ = 'usuario'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(Integer, nullable=False)
    subscription_date = Column(Integer, nullable=False)
    favorite = relationship('Favoritos', backref='usuario')

class Favoritos(Base):
    __tablename__ = 'favoritos'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('usuario.id'))
    planetas_favoritos = Column(String(250), nullable=False)
    personajes_favoritos = Column(String(250), nullable=False)
    planets = relationship('Planetas', backref='favoritos')
    perosnajes_fav = relationship('Personajes', backref='favoritos')

class Planetas(Base):
    __tablename__ = 'planetas'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    gravity = Column(String(250), nullable=False)
    population = Column(String(250), nullable=False)
    climate  = Column(String(250), nullable=False)
    fav_id = Column(Integer, ForeignKey('favoritos.planetas_favoritos'))
    
    
class Personajes(Base):
    __tablename__ = 'personajes'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    gender = Column(String(250),  nullable=False)
    eyes_color = Column(String(250), nullable=False)
    fav_id = Column(Integer, ForeignKey('favoritos.personajes_favoritos'))
    



def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
