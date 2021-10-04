from abc import ABC, abstractmethod
from datetime import datetime
from typing import List, Optional, Tuple

import config
from domain.model import Chat, StaffMember
from sqlalchemy.orm import Session

class AbstractRepository(ABC):
    @abstractmethod
    def add_chat(self, chat_id: int) -> bool:
        raise NotImplementedError

    @abstractmethod
    def del_chat(self, chat_id: int) -> bool:
        raise NotImplementedError

    @abstractmethod
    def get_chats(self) -> List[Chat]:
        raise NotImplementedError

    @abstractmethod
    def add_staff(self, user_id: int) -> bool:
        raise NotImplementedError

    @abstractmethod
    def del_staff(self, user_id: int) -> bool:
        raise NotImplementedError

    @abstractmethod
    def get_staff(self) -> List[StaffMember]:
        raise NotImplementedError



class SqlAlchemyRepository(AbstractRepository):
    session: Session

    def __init__(self, session: Session):
        self.session = session

    def add_chat(self, chat_id: int) -> bool:
        chat = self.session.query(Chat).filter_by(chat_id=chat_id).first()

        if chat is not None:
            return False

        chat = Chat(chat_id)
        self.session.add(chat)
        return True

    def del_chat(self, chat_id: int) -> bool:
        chat = self.session.query(Chat).filter_by(chat_id=chat_id).first()
        
        if chat is None:
            return False

        self.session.delete(chat)
        return True

    def get_chats(self) -> List[Chat]:
        chats = self.session.query(Chat).all()
        self.session.expunge_all()
        return chats


    def add_staff(self, user_id: int) -> bool:
        staff = self.session.query(StaffMember).filter_by(user_id=user_id).first()

        if staff is not None:
            return False

        staff = StaffMember(user_id)
        self.session.add(staff)
        return True

    def del_staff(self, user_id: int) -> bool:
        staff = self.session.query(StaffMember).filter_by(user_id=user_id).first()
        
        if staff is None:
            return False

        self.session.delete(staff)
        return True

    def get_staff(self) -> List[StaffMember]:
        staff_members = self.session.query(StaffMember).all()
        self.session.expunge_all()
        return staff_members



