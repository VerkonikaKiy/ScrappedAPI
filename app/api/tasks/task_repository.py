from sqlalchemy import select
from models.database import get_db
from models.models import task
from .task_schemas import AllTasks, CreateTask


class TaskRepository:
    @classmethod
    def add_task(cls, task_schema: CreateTask):
        with get_db() as session:
            data = task_schema.model_dump()
            new_task = task(**data)
            session.add(new_task)
            session.flush()
            session.commit()
            session.close()
            return new_task

    @classmethod
    def get_tasks(cls) -> list[AllTasks]:
        with get_db() as session:
            query = select(task)
            result = session.execute(query)
            task_models = result.scalars().all()
            tasks = [AllTasks.model_validate(task_model) for task_model in task_models]
            return tasks
