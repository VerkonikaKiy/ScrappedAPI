from pydantic import BaseModel
from datetime import time

from fastapi import Depends
from fastapi import APIRouter
from .task_schemas import CreateTask
from .task_repository import TaskRepository


task_router = APIRouter()


@task_router.get('/api/tasks')
def get_all_tasks():
    task_list = TaskRepository.get_tasks()
    return task_list


@task_router.post('/api/tasks')
def create_task(task_schema: CreateTask = Depends()):
    new_task = TaskRepository.add_task(task_schema)
    return {'id': new_task}
