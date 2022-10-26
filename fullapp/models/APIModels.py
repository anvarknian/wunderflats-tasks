from typing import Literal

from pydantic import BaseModel

CeleryStatus = Literal['PENDING', 'STARTED', 'RETRY', 'FAILURE', 'SUCCESS']

class WorkerPostResponse(BaseModel):
    id: str
    status: CeleryStatus

class Results(BaseModel):
    id: str
    status: str
    result: str