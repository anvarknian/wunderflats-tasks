from fastapi import APIRouter

from fullapp.spark.spark import spark_runner

router = APIRouter()

@router.get("/local_runner")
async def local_runner():
    spark_runner()
    return "Job Sent."
