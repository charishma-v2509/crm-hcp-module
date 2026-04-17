from sqlalchemy import Column, Integer, String
from app.database import Base

class HCP(Base):
    __tablename__ = "hcps"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    specialty = Column(String(100))
    hospital = Column(String(150))
    city = Column(String(100))
    email = Column(String(100))
    phone = Column(String(20))