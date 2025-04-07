from fastapi.encoders import jsonable_encoder
from uuid import UUID
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from fastapi import APIRouter
from starlette import status
from starlette.responses import JSONResponse
from .task_repository import TaskRepository
from models.database import get_db


single_task_router = APIRouter()


@single_task_router.get('/api/tasks/uuid')
def get_task(uuid: UUID, db: Session = Depends(get_db)):
    task = TaskRepository.get_task_info(db, uuid)
    if task is None:
        raise HTTPException(status_code=404, detail="Task does not exist")
    return JSONResponse(jsonable_encoder(task), status_code=status.HTTP_200_OK)


@single_task_router.delete('/api/tasks/uuid')
def delete_task(uuid: UUID, db: Session = Depends(get_db)):
    task = TaskRepository.delete_task(db, uuid)
    if task is None:
        raise HTTPException(status_code=404, detail="Task does not exist")
    return JSONResponse(jsonable_encoder(task), status_code=status.HTTP_204_NO_CONTENT)

