from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,DeclarativeBase
from sqlalchemy.pool import StaticPool


DATABASE_URL= "duckdb:///:memory:"

engine = create_engine(DATABASE_URL, 
                        poolclass=StaticPool)



SessionLocal=sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass


def init_db():
    from app.db.models import RunLog
    Base.metadata.create_all(bind=engine)


def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()