from pydantic import BaseModel, conint


class PageParams(BaseModel):
    page: conint(ge=0) = 0
    size: conint(ge=1, le=100) = 10

