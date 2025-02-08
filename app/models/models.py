from datetime import datetime

from sqlalchemy import URL, create_engine, text, Table, Column
from sqlalchemy import Integer, String, Boolean, MetaData, ForeignKey, Text, DateTime

import enum


metadata = MetaData()

post = Table('post', metadata,
    Column('uuid', Integer(), primary_key=True),
    Column('title', String(200), nullable=True),
    Column('preview_text', Text(),  nullable=True),
    Column('link', String(200), nullable=True),
    Column('is_new', Boolean(), default=True),
    Column('is_viewed', Boolean(), default=True),
)

post_info = Table('post_info', metadata,
    Column('uuid', Integer(), ForeignKey("post.uuid"), primary_key=True),
    Column('author_link', String(200), nullable=True),
    Column('author_name', String(200),  nullable=True),
    Column('text', Text(), nullable=True),
    Column('count_reactions', Integer(), default=True),
)

comment = Table('comment', metadata,
    Column('uuid', Integer(), primary_key=True),
    Column('author_link', String(200), nullable=True),
    Column('author_name', String(200),  nullable=True),
    Column('comment_text', Text(), nullable=True),
    Column('uuid_post_info', Integer(), ForeignKey("post_info.uuid")),
)

task = Table('task', metadata,
    Column('uuid', Integer(), primary_key=True),
    Column('site_link', String(200), nullable=True),
    Column('start_time', DateTime(), default=datetime.now),
    Column('end_time', DateTime(), default=datetime.now),
    Column('status', String(200)),
    Column('last_post_id', Integer()),
)

