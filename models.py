from sqlalchemy import Column, Integer, String, Boolean, Date, Interval, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from db import engine

# Create a declarative base class for table definitions.
Base = declarative_base()

# Define models
class Nadador(Base):
    __tablename__ = 'Nadadores'

    id = Column(Integer, primary_key=True)
    nombreApellido = Column(String)
    sexo = Column(Boolean)
    categoria = Column(String)
    club = Column(String)

    # Establish a many-to-many relationship with Pruebas.
    pruebas = relationship('Nadadores_Pruebas', back_populates='nadadores_pruebas')

class Prueba(Base):
    __tablename__ = 'Pruebas'

    id = Column(Integer, primary_key=True)
    descripcion = Column(String)

    # Establish a many-to-many relationship with Nadadores.
    nadadores = relationship('Nadadores_Pruebas', back_populates='pruebas_nadadores')

class Nadadores_Pruebas(Base):
    __tablename__ = 'Nadadores_Pruebas'
    
    id = Column(Integer, primary_key=True)
    idNadador = Column(Integer, ForeignKey('Nadadores.id'))
    idPrueba = Column(Integer, ForeignKey('Pruebas.id'))
    fecha = Column(Date)
    tiempoPreInscripcion = Column(Interval)
    tiempoCompeticion = Column(Interval)

# Create the tables in the database 
Base.metadata.create_all(engine, checkfirst=True)
