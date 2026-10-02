import sys
from celery.__main__ import main


def start_worker():
    sys.argv = ["celery", "-A", "backend", "worker", "--loglevel=info", "-P", "threads"]
    main()


def start_flower():
    sys.argv = ["celery", "-A", "backend", "flower", "--port=5555", "--loglevel=info"]
    main()
