from datetime import datetime
from dataclasses import dataclass


@dataclass()
class Chat:
    chat_id: int

@dataclass()
class StaffMember:
    user_id: int
