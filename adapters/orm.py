from sqlalchemy import (
    Table,
    MetaData,
    Column,
    Integer,
)
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import mapper

from domain.model import Chat, StaffMember
import config

metadata = MetaData()

chat = Table(
    "chats",
    metadata,
    Column("chat_id", Integer, primary_key=True, autoincrement=False),
)

staff_member = Table(
    "staff_members",
    metadata,
    Column("user_id", Integer, primary_key=True, autoincrement=False),
)

def start_mappers():
    mapper(Chat, chat)
    mapper(StaffMember, staff_member)


def create_tables():
    engine = create_engine(config.get_sqlite_uri())
    metadata.create_all(engine)
