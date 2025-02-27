from pydantic import BaseModel
from datetime import time


class BaseTask(BaseModel):
    site_link: str
    start_time: time
    end_time: time
    status: str
    last_post_id: int


class CreateTask(BaseTask):
    pass


class AllTasks(BaseTask):
    id: int