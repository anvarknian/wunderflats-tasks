from fastapi import FastAPI

from fullapp.models.monitor import Health
from fullapp.routes.celery_runner_endpoint import router as cr
from fullapp.routes.get_results_endpoint import router as gr
from fullapp.routes.local_runner_endpoint import router as lr
from fullapp.routes.monitor import health_check
from starlette_prometheus import metrics

app = FastAPI(title="W U N D E R F L A T", version="0.1.0")
# noinspection PyTypeChecker
app.add_api_route("/metrics", metrics)
app.add_api_route("/health",
                  health_check,
                  response_model=Health)

app.include_router(cr)
app.include_router(lr)
app.include_router(gr)

# app.include_router(add_new_project)
