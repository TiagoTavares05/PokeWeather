from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from config import database_url

Base = declarative_base()
engine = create_engine(database_url)
Session = sessionmaker(bind=engine)

class Trainer(Base):
    __tablename__ = "trainers"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    pokemons = relationship("Pokemon", back_populates="trainer")

class Pokemon(Base):
    __tablename__ = "pokemons"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    type = Column(String)
    trainer_id = Column(Integer, ForeignKey("trainers.id"))
    trainer = relationship("Trainer", back_populates="pokemons")

def init_db():
    Base.metadata.create_all(engine)