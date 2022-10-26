from fastapi import APIRouter

from fullapp.celery_app import spark_on_celery_job
from fullapp.models.APIModels import WorkerPostResponse

router = APIRouter()


@router.post("/celery_runner", response_model=WorkerPostResponse)
async def celery_runner():
    task = spark_on_celery_job.delay()
    return WorkerPostResponse(id=task.id,
                   status=task.status)
