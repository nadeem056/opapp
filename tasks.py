#!/usr/bin/python3
import json
from celery import Celery
from bookplayer import playthebook as pbk
from bookplayer import ResultCallback
from random import randint
from time import ctime, sleep

BROKER_URL = "redis://localhost:6379/0"
BACKEND_URL = 'redis://localhost:6379/1'
celery = Celery('tasks', broker=BROKER_URL, backend=BACKEND_URL)


@celery.task
def add(x,y):
  objc= { "A": x, "B": y, "Sum": x+y }
  return objc

@celery.task
def play():
  ex=pbk('paly.yml','192.168.56.101')  
  # The  playbook and inventory is hadcoded for now in bookexecutor
  result=ex.run()
  print(dir(ex._tqm._stdout_callback))  # To View in logs (to be removed)
  task_res=ex._tqm._stdout_callback.task_results
  print('>>> ', tres)   # To View in logs (to be removed)
  return { "result": task_res }
