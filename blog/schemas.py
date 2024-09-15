from typing import List
from pydantic import BaseModel


class Blog(BaseModel):
    title: str
    desc: str


class UserBase(BaseModel):
    email: str
    name: str


class User(UserBase):
    password: str


class ShowUser(BaseModel):
    email: str
    name: str
    blogs: List[Blog]


class ShowBlog(BaseModel):
    title: str
    desc: str
    creator: UserBase


class Login(BaseModel):
    email: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None
