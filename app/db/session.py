import pymysql
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

pymysql.install_as_MySQLdb()

engine = create_engine(
    settings.DATABASE_URL,
    echo=settings.DATABASE_ECHO,
    pool_pre_ping=True,
    pool_recycle=3600,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
