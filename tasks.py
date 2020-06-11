#!/usr/bin/python3
from celery import Celery
from anible import playthebook as pbk
BROKER_URL = "redis://localhost:6379/0"
BACKEND_URL = 'redis://localhost:6379/1'
celery = Celery('tasks', broker=BROKER_URL, backend=BACKEND_URL)
@celery.task
def add(x,y):
  return x+y

@celery.task
def play():
  return pbk()
