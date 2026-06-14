from sqlalchemy import Column,Integer,String,ForeignKey
from database import Base

class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True,index=True)

    username = Column(String)

    password = Column(String)


class Note(Base):

    __tablename__ = "notes"

    id = Column(Integer, primary_key=True,index=True)

    title = Column(String)

    content = Column(String)

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )