from .celery_app import app as celery_app


# to make sure that celery is always imported when django starts. 
__all__ = ("celery_app",)