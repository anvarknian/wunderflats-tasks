import sys

import uvicorn
from fullapp.celery_app import celery_app

def uvicorn_runner():
    uvicorn.run("fullapp.app:app",
                host='0.0.0.0',
                port=8080,
                reload=True)

def worker_runner():
    argv = [
        'worker',
        '--loglevel=INFO',
        '--autoscale=3,10',
    ]

    celery_app.worker_main(argv)


if __name__ == '__main__':
    if sys.argv[1] == "api":
        uvicorn_runner()
    elif sys.argv[1] == "worker":
        worker_runner()
