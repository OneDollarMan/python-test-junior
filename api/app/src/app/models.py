from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
import uuid
from ..init_database import Base


class UserEventModel(Base):
	__tablename__ = 'Events'
	id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
	date_created = Column(DateTime)
	user_ip = Column(String)
