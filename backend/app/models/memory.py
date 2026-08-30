from sqlalchemy import Column, String, DateTime, Text
from datetime import datetime, timezone
import uuid

from ..core.database import Base

class UserMemory(Base):
    """
    SQLAlchemy Model for persistent user context / memory bank.
    Injects context automatically into future generations.
    """
    __tablename__ = "user_memories"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, index=True, default="default_user", nullable=False)
    
    key = Column(String, index=True, nullable=False)
    value = Column(Text, nullable=False)
    context_category = Column(String, default="profile")
    
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
