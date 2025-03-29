from typing import Sequence
from uuid import UUID
from api.pagination.paginate import paginate
from sqlalchemy import select
from sqlalchemy.orm import Session
from models.models import Task
from .task_schemas import BaseTask
from ..pagination.pagination_schema import PageParams


class TaskRepository:
    @classmethod
    def add_task(cls, task_schema: BaseTask, db: Session):
        data = task_schema.model_dump()
        new_task = Task(**data)
        db.add(new_task)
        db.commit()
        return new_task

    @classmethod
    def get_tasks(cls, page_params: PageParams, db: Session) -> Sequence[Task]:
        data = db.execute(select(Task)).scalars().all()
        return paginate(page_params, data)

    @classmethod
    def get_task_info(cls, db: Session, uuid: UUID) -> Sequence[Task]:
        return db.execute(select(Task).filter_by(uuid=uuid)).scalar()

    @classmethod
    def delete_task(cls, db: Session, uuid: UUID) -> Sequence[Task]:
        task = db.execute(select(Task).filter_by(uuid=uuid)).scalar()
        db.delete(task)
        db.commit()
        return {"response": "deleted"}
