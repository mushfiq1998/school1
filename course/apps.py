# https://github.com/django/django/blob/main/django/apps/config.py
from django.apps import AppConfig


class CourseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'course'
