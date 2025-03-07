from typing import Sequence

from sqlalchemy import select
from sqlalchemy.orm import Session

from models.database import get_db
from models.models import Task
from .task_schemas import AllTasks, CreateTask


class TaskRepository:
    @classmethod
    def add_task(cls, task_schema: CreateTask, db: Session):
        data = task_schema.model_dump()
        new_task = Task(**data)
        db.add(new_task)
        db.commit()
        return new_task

    @classmethod
    def get_tasks(cls, task_schema: AllTasks, db: Session) -> Sequence[Task]:
        return db.execute(select(Task)).scalars().all()

    @classmethod
    def get_task_info(cls, db: Session, uuid) -> Sequence[Task]:
        return db.execute(select(Task).filter_by(uuid=uuid)).scalar()
