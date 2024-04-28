import config

"""
SQLAlchemy Configuration
- use sqlite3
"""
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine
engine = create_engine(f'sqlite:///{config.llm_db_name}')
Session = sessionmaker(bind=engine)

