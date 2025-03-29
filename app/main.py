from fastapi import FastAPI, Depends, APIRouter
import os
from typing import Optional

from fastapi_pagination import add_pagination

from api.tasks import all_tasks, task_info


app = FastAPI()
app.include_router(all_tasks.task_router)
app.include_router(task_info.single_task_router)

add_pagination(app)

router = APIRouter()


@router.get('/')
def test():
    return {'data': 'ps'}
