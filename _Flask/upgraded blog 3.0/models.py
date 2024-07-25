from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text, ForeignKey
from typing import List
from flask_login import UserMixin


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


# CONFIGURE TABLES
class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    author: Mapped["User"] = relationship(back_populates="blogposts")
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)
    comments: Mapped[List["Comment"]] = relationship(back_populates="post")


# TODO: Create a User table for all your registered users.
# CREATE TABLE IN DB
class User(db.Model, UserMixin):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(100), nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    blogposts: Mapped[List["BlogPost"]] = relationship(back_populates="author")
    comments: Mapped[List["Comment"]] = relationship(back_populates="author")


class Comment(db.Model):
    __tablename__ = "comments"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    author: Mapped["User"] = relationship(back_populates="comments")
    post_id: Mapped[int] = mapped_column(ForeignKey("blog_posts.id"))
    post: Mapped["BlogPost"] = relationship(back_populates="comments")
