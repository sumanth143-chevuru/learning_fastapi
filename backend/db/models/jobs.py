from sqlalchemy import Column, Integer, String, Boolean,Date, ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base


class Job(Base):
    id = Column(Integer,primary_key = True, index=True)
    title = Column(String(255),nullable= False)
    company = Column(String(255),nullable=False)
    company_url = Column(String(255))
    location = Column(String(255),nullable = False)
    description = Column(String(255),nullable=False)
    date_posted = Column(Date)
    is_active = Column(Boolean(),default=True)
    owner_id =  Column(Integer,ForeignKey("user.id"))
    owner = relationship("User",back_populates="jobs")
