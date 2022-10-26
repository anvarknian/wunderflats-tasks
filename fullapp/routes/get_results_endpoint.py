from celery.result import AsyncResult
from fastapi import APIRouter

from fullapp.models.APIModels import Results

router = APIRouter()


# Method used to check any celery status/result

@router.get("/get_result", response_model=Results)
async def get_result(task_id: str):
    task = AsyncResult(id=task_id)
    return Results(id=task.id,
                   status=task.status,
                   result=task.result)
