from fastapi import FastAPI, Depends
import os
from typing import Optional
from api.tasks import all_tasks


app = FastAPI()
app.include_router(all_tasks.router)


