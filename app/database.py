from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import local_settings as ls

SQLALCHEMY_DATABASE_URL = f'postgresql://{ls.user}:{ls.password}@{ls.host}/{ls.database}'
engine = create_engine(
    # SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

print("Crear modulo de usuarios, obtener rutas")