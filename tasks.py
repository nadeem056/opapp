#!/usr/bin/python3
import json
from celery import Celery
from bookplayer import playthebook as pbk
from time import ctime, sleep

#BROKER_URL = "redis://localhost:6379/0"
#BACKEND_URL = 'redis://localhost:6379/1'
BROKER_URL  = "redis://192.168.56.103:6379/0"
BACKEND_URL = "redis://192.168.56.103:6379/1"
celery = Celery('tasks', broker=BROKER_URL, backend=BACKEND_URL)


@celery.task
def add(x,y):
  objc= { "A": x, "B": y, "Sum": x+y }
  return objc

@celery.task
def play():
  res,ex=pbk()
  # The  playbook and inventory is hadcoded for now in bookexecutor
  task_res=ex._tqm._stdout_callback.task_result
  return { "stdout": task_res[0].get('stdout') }
