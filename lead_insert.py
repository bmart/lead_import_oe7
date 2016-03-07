from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import sessionmaker

# Fill in these 3 parameters
db_user = ""
db_pass = ""
db_name = ""

engine  = create_engine('postgresql://%s:%s@localhost/%s' % (db_user, db_pass, db_name))
Base    = declarative_base()
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

class CrmLead(Base):
    """more columns exist, but these are the only ones I am using right now"""
    __tablename__ = "crm_lead"
    id      = Column(Integer, primary_key=True)
    name    = Column(String)
    active  = Column(Boolean)


db_session = Session()

lead        = CrmLead()
lead.name   = "My new lead"
lead.active = True

db_session.add(lead)
db_session.commit()
