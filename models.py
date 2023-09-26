"""Modelos a representar en la base de datos"""

from sqlalchemy import Column, Integer, String, Boolean, Date, Interval, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from db import engine

# Create a declarative base class for table definitions.
Base = declarative_base()

# Define models
class Nadador(Base):
    """Clase que representa un Nadador"""
    __tablename__ = 'Nadadores'

    id = Column(Integer, primary_key=True)
    nombreApellido = Column(String)
    sexo = Column(Boolean)
    categoria_id = Column(Integer, ForeignKey('Categorias.id'))
    club_id = Column(Integer, ForeignKey('Clubes.id'))

    categoria = relationship('Categoria', back_populates='nadadores')
    club = relationship('Club', back_populates='nadadores')
    pruebas = relationship('Nadadores_Pruebas', back_populates='nadadores_pruebas')

class Prueba(Base):
    """Clase que representa una Prueba (por ejemplo 25m mariposa)"""
    __tablename__ = 'Pruebas'

    id = Column(Integer, primary_key=True)
    descripcion = Column(String)

    # Establish a many-to-many relationship with Nadadores.
    nadadores = relationship('Nadadores_Pruebas', back_populates='pruebas_nadadores')

class Categoria(Base):
    """Clase que representa una Categoria (A, B, C)"""
    __tablename__ = 'Categorias'

    id = Column(Integer, primary_key=True)
    descripcion = Column(String)
    nadadores = relationship('Nadador', back_populates='categoria')

class Club(Base):
    """Clase que representa un Club"""
    __tablename__ = 'Clubes'

    id = Column(Integer, primary_key=True)
    descripcion = Column(String)
    nadadores = relationship('Nadador', back_populates='clubes')

class NadadoresPruebas(Base):
    """Clase que representa la relación entre nadadores y pruebas"""
    __tablename__ = 'Nadadores_Pruebas'
    
    id = Column(Integer, primary_key=True)
    idNadador = Column(Integer, ForeignKey('Nadadores.id'))
    idPrueba = Column(Integer, ForeignKey('Pruebas.id'))
    fecha = Column(Date)
    tiempoPreInscripcion = Column(Interval)
    tiempoCompeticion = Column(Interval)

# Create the tables in the database 
Base.metadata.create_all(engine, checkfirst=True)
