from sqlalchemy.orm import relationship
from .database import Base
from sqlalchemy import Column, ForeignKey, Integer, String


class Blog(Base):
    __tablename__ = "blogs"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    title = Column(String, nullable=False)
    desc = Column(String, nullable=False)
    # This relationship will allow us to access ceator of blog whenever
    # we want to and only fetches the user if we try to access it
    creator = relationship("User", back_populates="blogs")
    user_id = Column(Integer, ForeignKey("users.id"))


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    blogs = relationship("Blog", back_populates="creator")
