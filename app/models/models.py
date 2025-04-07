import uuid
from datetime import datetime

from sqlalchemy import Integer, String, DateTime, Enum, MetaData, Text, Boolean, ForeignKey
from sqlalchemy import Table, Column
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base

ModelBase = declarative_base()


metadata = MetaData()
class Post(ModelBase):
    __tablename__ = 'post'
    uuid = Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True, unique=True)
    title = Column(String(200), nullable=True)
    preview_text = Column(Text(), nullable=True)
    link = Column(String(200), nullable=True)
    is_new = Column(Boolean(), default=True)
    is_viewed = Column(Boolean(), default=True)


class PostInfo(ModelBase):
    __tablename__ = 'post_info'
    uuid = Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True, unique=True)
    author_link = Column(String(200), nullable=True)
    author_name = Column(String(200), nullable=True)
    text = Column(Text(), nullable=True)
    count_reactions = Column(Integer(), nullable=True)
    uuid_post = Column(UUID(as_uuid=True), ForeignKey("post.uuid"))


class Comment(ModelBase):
    __tablename__ = 'comment'
    uuid = Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True, unique=True)
    author_link = Column(String(200), nullable=True)
    author_name = Column(String(200), nullable=True)
    comment_text = Column(Text(), nullable=True)
    uuid_post_info = Column(UUID(as_uuid=True), ForeignKey("post_info.uuid"))


class Task(ModelBase):
    __tablename__ = 'task'
    uuid = Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True, unique=True)
    site_link = Column(String(200), nullable=True)
    start_time = Column(DateTime, default=datetime.now)
    end_time = Column(DateTime, nullable=True)
    status = Column(String, default="Not started")
    last_post_id = Column(Integer, nullable=True)
