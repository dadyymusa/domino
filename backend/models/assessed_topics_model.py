from sqlalchemy import Column, INTEGER, String
from db.config import Base

class Assessed_Topics(Base):
    
    __tablename__ = 'assessed_topics'

    id = Column(INTEGER, primary_key = True, index = True)
    date = Column(String)
    topics = Column(String)
    subject = Column(String)
    