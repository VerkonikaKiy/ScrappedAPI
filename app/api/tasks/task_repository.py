from typing import Sequence
from uuid import UUID

from fastapi.encoders import jsonable_encoder
from sqlalchemy import select
from sqlalchemy.orm import Session

from models.database import get_db, SessionLocal
from models.models import Task
from .task_schemas import BaseTask


class TaskRepository:
    @classmethod
    def add_task(cls, task_schema: BaseTask, db: Session):
        data = task_schema.model_dump()
        new_task = Task(**data)
        db.add(new_task)
        db.commit()

    @classmethod
    def get_task_info(cls, db: Session, uuid: UUID) -> Sequence[Task]:
        return db.execute(select(Task).filter_by(uuid=uuid)).scalar()

    @classmethod
    def get_task_by_status(cls, status: str) -> Sequence[Task]:
        with SessionLocal() as db:
            try:
                task = db.query(Task).filter_by(status=status).all()
                return task
            except task is None: print(f'Tasks with satus {status} not found')

    @classmethod
    def change_task_status(cls, uuid, token):
        with SessionLocal() as db:
            task = db.query(Task).filter_by(uuid=uuid).first()
            if task:
                if token == 'sent_to_execute':
                    task.status = 'in_progress'
                elif token == 'recieved_failed':
                    task.status = 'failed'
                elif token == 'recieved_success':
                    task.status = 'successful'
                db.commit()
                new_status_task = db.query(Task).filter_by(uuid=uuid).first()
                return jsonable_encoder(new_status_task)
                # print('task changed')


    @classmethod
    def delete_task(cls, db: Session, uuid: UUID) -> Sequence[Task]:
        task = db.execute(select(Task).filter_by(uuid=uuid)).scalar()
        db.delete(task)
        db.commit()
        return {"response": "deleted"}
