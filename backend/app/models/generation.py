from sqlalchemy import Column, String, DateTime, Text, Integer, Boolean
from datetime import datetime, timezone
import uuid

from ..core.database import Base

class Generation(Base):
    __tablename__ = "generations"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, index=True, default="default_user", nullable=False)
    platform = Column(String)
    content_type = Column(String)
    tone = Column(String)
    audience = Column(String)
    length = Column(String)
    custom_prompt = Column(Text, nullable=True)
    generated_content = Column(Text)
    version = Column(Integer, default=1)
    is_favorite = Column(Boolean, default=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
