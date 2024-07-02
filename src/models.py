import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

Favorite = Table(
    'favorite',
    Base.metadata,
    Column('planets_id', Integer, ForeignKey('usuario.id')),
    Column('people_id', Integer, ForeignKey('usuario.id'))
)
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
    planetas = relationship('Planetas', backref='usuario', lazy=True)
    Personajes = relationship('Personajes', backref='usuario', lazy=True)
    favorites = relationship(
         'Usuario',
         secondary=Favorite,
         primaryjoin=(Favorite.c.planets_id == id),
         secondaryjoin=(Favorite.c.people_id == id),
         backref='favor',
         lazy=True

    )


class Planetas(Base):
    __tablename__ = 'planetas'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, ForeignKey("Usuario.id"), primary_key=True)
    Abafar = Column(String(250), ForeignKey("Favoritos.planets"))
    Agamar = Column(String(250), nullable=False)
    Ahch_To = Column(String(250), nullable=False)
    Ajan  = Column(String(250), nullable=False)
    Akiva = Column(String(250), nullable=False)
    Abafar = Column(String(250), ForeignKey("Favoritos.planets"))
    usuario = relationship(Usuario)
    Favorite = relationship(Favorite)
    
class Personajes(Base):
    __tablename__ = 'personajes'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, ForeignKey("planeta.id"), primary_key=True)
    Jabba = Column(String(250), ForeignKey("Planeta.Agamar"))
    Ezra = Column(String(250),  ForeignKey("Planeta.Akiva"), nullable=False)
    Anakin = Column(String(250), nullable=False)
    Chewbacca = Column(String(250), ForeignKey("Favoritos.people"), nullable=False)
    Luke = Column(String(250), nullable=False)
    Han = Column(String(250), ForeignKey("Planeta.Ajan"))
    Princesa_Leia = Column(String(250),  nullable=False)
    usuario = relationship(Usuario)
    Planetas = relationship(Planetas)
    Favorite = relationship(Favorite)

class Favoritos(Base):
    __tablename__ = 'favoritos'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    planets = Column(String(250), ForeignKey("Planeta.Alderaan"), primary_key=True)
    people = Column(String(250), ForeignKey("Personajes.Princesa_Leia"), primary_key=True)
 


def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
