from pdf_analyzer.models import Message
from sqlmodel import Session, select
from uuid import UUID
from typing import Sequence


class MessageRepository:

    def save_messages(self, session: Session, *message: Message):
        for msg in message:
            session.add(msg)

        session.commit()

        for msg in message:
            session.refresh(msg)

    def find_chat_by_id(self, session: Session, chat_id: UUID) -> Sequence[Message]:
        return session.exec(select(Message)).all()