from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

"""
Configuration for the SQLAlchemy database URL.
This URL specifies that SQLAlchemy should use a SQLite database located in the current directory.
"""
SQLALCHEMY_DATABASE_URL = "sqlite:///./books.db"

"""
The engine is responsible for managing the connection to the database.
`create_engine` creates an instance that will interface with the DBAPI, using the connection parameters provided.
The `connect_args` argument is specific to SQLite; it allows multiple threads to share the same connection.
"""
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

"""
A sessionmaker instance establishes all conversations with the database
and represents a "staging zone" for all the objects loaded into the database session object.
Any changes made against the objects in the session won't be persisted into the database until you call
`session.commit()`. If you're not happy about the changes, you can revert all of them back to the
last commit by calling `session.rollback()`.
"""
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

"""
The declarative base class will be used as a base class for all model classes.
This class maintains a catalog of classes and tables relative to that base - this is known as the declarative registry.
"""
Base = declarative_base()

# Definition of the Book model class.
# Each class variable represents a column in the database table.
class Book(Base):
    __tablename__ = "books"  # Specifies the name of the table in the database

    id = Column(Integer, primary_key=True, index=True)  # Primary key, automatically indexed.
    title = Column(String, index=True)  # Title of the book; `index=True` makes lookups to this column faster.
    author = Column(String, index=True) 
    rating = Column(Float) 

# Function to create the database and tables.
def create_db_and_tables():
    # This function will create all the tables defined by the models which inherit from `Base`.
    # It binds the engine (connection and DBAPI configuration) to the metadata of the base class,
    # which effectively creates the schema in the database for all inherited models.
    Base.metadata.create_all(bind=engine)
