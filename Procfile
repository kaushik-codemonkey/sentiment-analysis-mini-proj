web: gunicorn app:app --workers 1
worker: celery -A celery_app.celery worker --loglevel=info
