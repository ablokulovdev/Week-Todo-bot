from datetime import datetime
from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    BigInteger,
    DateTime,
    Text
)
from sqlalchemy.orm import DeclarativeBase,relationship

class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"
    
    id          = Column(Integer,primary_key=True)
    telegram_id = Column(BigInteger,nullable=False,index=True)
    first_name  = Column(String(150),nullable=False,unique=True)
    last_name   = Column(String(150))
    username    = Column(String(150))
    
    updated_at  = Column(DateTime,default=datetime.utcnow)
    created_at  = Column(DateTime,onupdate=datetime.utcnow)
    
    tasks       = relationship("Task",back_populates="user")
    
    def __repr__(self):
        return f"User (id={self.id}, telegram_id={self.telegram_id}, first_name = {self.first_name})"
    
    
class Task(Base):
    __tablename__ = "tasks"
    
    id          = Column(Integer,primary_key=True)
    name        = Column(String(150),nullable=False,index=True)
    description = Column(Text)
    user_id     = Column(ForeignKey("users.id",ondelete="CASCADE"))
    
    user        = relationship("User",back_populates="tasks")
    
    
    updated_at  = Column(DateTime,default=datetime.utcnow)
    created_at  = Column(DateTime,onupdate=datetime.utcnow)
    