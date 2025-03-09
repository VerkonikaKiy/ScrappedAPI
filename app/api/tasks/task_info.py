from fastapi.encoders import jsonable_encoder
from uuid import UUID, uuid4

from sqlalchemy.orm import Session
from fastapi import Depends
from fastapi import APIRouter
from starlette import status
from starlette.responses import JSONResponse

from .task_repository import TaskRepository
from models.database import get_db
from .task_schemas import AllTasks


single_task_router = APIRouter()


@single_task_router.get('/api/tasks/{uuid}')
def get_task(uuid: uuid4, db: Session = Depends(get_db)):
    task = TaskRepository.get_task_info(uuid, db)
    return JSONResponse(jsonable_encoder(task), status_code=status.HTTP_200_OK)
