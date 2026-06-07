from sqlalchemy import Column ,Integer, String,Float,DateTime,Sequence
from sqlalchemy.sql import func
from app.db.database import Base


class RunLog(Base):
    __tablename__="run_logs"
    id = Column(Integer,Sequence('run_log_id_seq'),primary_key=True)
    status= Column(String,nullable=False)
    duration=Column(Float,nullable=True)
    output= Column(String,nullable=True)
    created_at = Column(DateTime,server_default=func.now())


