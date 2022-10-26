from __future__ import absolute_import, unicode_literals

from celery import Celery

from fullapp.spark.spark import spark_runner

celery_app = Celery("WUNDERFLAT - CELERY",
                    broker="redis://redis:6379/0",
                    backend="redis://redis:6379/0",
                    task_track_started=True)

celery_app.autodiscover_tasks()


@celery_app.task(name='spark_on_celery_job',
                 bind=True)
def spark_on_celery_job(self):
    spark_runner()
    return "SUCCESS"
