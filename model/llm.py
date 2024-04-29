from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class LLM(Base):
    __tablename__ = 'llm'
    model_name    = Column(String, primary_key=True)
    chat_template = Column(String)
    nickname      = Column(String)

