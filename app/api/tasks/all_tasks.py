from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from datetime import time

from sqlalchemy.orm import Session
from fastapi import Depends
from fastapi import APIRouter
from starlette import status
from starlette.responses import JSONResponse

from .task_schemas import CreateTask, AllTasks
from .task_repository import TaskRepository
from models.database import get_db


task_router = APIRouter()


@task_router.get('/api/tasks')
def get_all_tasks(task_schema: AllTasks, db: Session = Depends(get_db)):
    task_list = TaskRepository.get_tasks(task_schema, db)
    return JSONResponse(jsonable_encoder(task_list), status_code=status.HTTP_200_OK)


@task_router.post('/api/tasks')
def create_task(task_schema: CreateTask = Depends(), db: Session = Depends(get_db)):
    new_task = TaskRepository.add_task(task_schema, db)
    return JSONResponse(jsonable_encoder(new_task), status_code=status.HTTP_201_CREATED)
