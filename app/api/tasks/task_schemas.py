from datetime import date
from uuid import UUID, uuid4
from pydantic import BaseModel
from datetime import datetime


class BaseTask(BaseModel):
    uuid: UUID = uuid4()
    site_link: str
    start_time: datetime
    end_time: datetime
    status: str
    last_post_id: int


class CreateTask(BaseTask):
    pass


class AllTasks(BaseTask):
    uuid: UUID = uuid4()
