from fastapi.encoders import jsonable_encoder
from fastapi_pagination import pagination_ctx, Page, Params, set_page
from sqlalchemy.exc import IntegrityError

from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from fastapi import APIRouter
from starlette import status
from starlette.responses import JSONResponse

from models.models import Task
from .task_schemas import BaseTask
from .task_repository import TaskRepository
from models.database import get_db
from fastapi_pagination.ext.sqlalchemy import paginate

task_router = APIRouter()


@task_router.get('/api/tasks', dependencies=[
        Depends(
            pagination_ctx(
                page=Page[int],
                params=Params,
            ),
        ),
    ])
def get_all_tasks(db: Session = Depends(get_db)):
    query = db.query(Task)
    set_page(Page[BaseTask])
    paginated_data = paginate(db, query)
    response_data = {
        "items": [jsonable_encoder(item) for item in paginated_data.items],
        "total": paginated_data.total,
        "page": paginated_data.page,
        "size": paginated_data.size,
        "pages": paginated_data.pages,
    }
    return JSONResponse(response_data, status_code=status.HTTP_200_OK)


@task_router.post('/api/tasks')
def create_task(task_schema: BaseTask = Depends(), db: Session = Depends(get_db)):
    try:
        new_task = TaskRepository.add_task(task_schema, db)
    except IntegrityError:
        raise HTTPException(status_code=400, detail="Incorrect request data")
    return JSONResponse(jsonable_encoder(new_task), status_code=status.HTTP_201_CREATED)
