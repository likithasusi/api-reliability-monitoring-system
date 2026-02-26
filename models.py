from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from app.database import Base

class MonitoredAPI(Base):
    __tablename__ = "monitored_apis"

    id = Column(Integer, primary_key=True, index=True)
    api_name = Column(String, unique=True, index=True)
    url = Column(String)
    expected_status = Column(Integer)


class APIHealthLog(Base):
    __tablename__ = "api_health_logs"

    id = Column(Integer, primary_key=True, index=True)
    api_name = Column(String)
    status = Column(String)
    response_time = Column(Float)
    checked_at = Column(DateTime, default=datetime.utcnow)