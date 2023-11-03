import sqlalchemy
from sqlalchemy import Column, String, DateTime, create_engine
from sqlalchemy.dialects.postgresql import UUID
import uuid
from sqlalchemy.orm import sessionmaker, declarative_base
from db_config import db_settings

engine = create_engine(db_settings.data_source_name, echo=False)
Session = sessionmaker(bind=engine, expire_on_commit=False)
Base = declarative_base(metadata=sqlalchemy.MetaData())


class UserEventModel(Base):
    __tablename__ = 'Events'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    date_created = Column(DateTime)
    user_ip = Column(String)
