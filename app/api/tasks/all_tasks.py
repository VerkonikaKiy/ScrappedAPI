from fastapi.encoders import jsonable_encoder
from fastapi_pagination.ext import sqlalchemy
from sqlalchemy.exc import IntegrityError

from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from fastapi import APIRouter
from starlette import status
from starlette.responses import JSONResponse

from .task_schemas import BaseTask
from .task_repository import TaskRepository
from models.database import get_db
from models.models import Task
from ..pagination.pagination_schema import PageParams

task_router = APIRouter()


@task_router.get('/api/tasks')
def get_all_tasks(page_params: PageParams = Depends(), db: Session = Depends(get_db)):
    task_list = TaskRepository.get_tasks(page_params, db)
    return JSONResponse(task_list, status_code=status.HTTP_200_OK)


@task_router.post('/api/tasks')
def create_task(task_schema: BaseTask = Depends(), db: Session = Depends(get_db)):
    try:
        new_task = TaskRepository.add_task(task_schema, db)
    except IntegrityError:
        raise HTTPException(status_code=400, detail="Incorrect request data")
    return JSONResponse(jsonable_encoder(new_task), status_code=status.HTTP_201_CREATED)
