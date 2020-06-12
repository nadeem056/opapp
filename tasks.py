#!/usr/bin/python3
import json
from celery import Celery
from bookplayer import playthebook as pbk
from random import randint
from time import ctime, sleep

BROKER_URL = "redis://localhost:6379/0"
BACKEND_URL = 'redis://localhost:6379/1'
celery = Celery('tasks', broker=BROKER_URL, backend=BACKEND_URL)
@celery.task
def add(x,y):
  return {"blue": "red"}

@celery.task
def play():
  r=pbk('', '')
  print(type(r))
  print(r)
  # jr=json.loads(r)
  # print(type(jr))
  return { "stdout": r }
