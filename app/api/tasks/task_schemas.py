from enum import Enum
from uuid import UUID, uuid4
from pydantic import BaseModel, field_validator, ConfigDict
from datetime import datetime


class Status(str, Enum):
    not_started = 'not_started'
    in_progress = 'in_progress'
    failed = 'failed'
    successfull = 'successfull'

class SiteLink(str, Enum):
    habr = 'https://habr.com/'
    tprogger = 'https://tproger.ru/'
    proglib = 'https://proglib.io/'

class BaseTask(BaseModel):
    uuid: UUID = uuid4()
    site_link: SiteLink
    start_time: datetime
    end_time: datetime
    status: Status
    last_post_id: int

    model_config = ConfigDict(from_attributes=True)

    @field_validator('start_time')
    def start_time_validate(cls, time: datetime):
        if time > datetime.now():
            raise ValueError('time value cannot be later then current time')
        return time
