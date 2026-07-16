from sqlalchemy import Column,Integer,String,ForeignKey,DateTime,Text
from database import Base
from datetime import datetime
from sqlalchemy.orm import relationship

class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True,index=True)

    username = Column(String, unique=True)

    password = Column(String)

    email = Column(String, unique=True, nullable=True)

    role = Column(String, default="user")

    notes = relationship(
    "Note",
    back_populates="owner"
)


class Note(Base):

    __tablename__ = "notes"

    id = Column(Integer, primary_key=True,index=True)

    title = Column(String)

    content = Column(String)

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    owner = relationship(
    "User",
    back_populates="notes"
)
    
class Conversation(Base):

    __tablename__ = "conversations"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    session_id = Column(
        String,
        unique=True,
        nullable=False,
        index=True
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    messages = relationship(
        "ChatMessage",
        back_populates="conversation",
        cascade="all, delete"
    )

class ChatMessage(Base):

    __tablename__ = "chat_messages"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    conversation_id = Column(
        Integer,
        ForeignKey("conversations.id")
    )

    role = Column(
        String,
        nullable=False
    )

    content = Column(
        Text,
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    conversation = relationship(
        "Conversation",
        back_populates="messages"
    )