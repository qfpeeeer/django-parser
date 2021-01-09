from time import sleep

from celery import shared_task

from .com.parser_mechta import parse
from celery.schedules import crontab
from celery.task import periodic_task


@periodic_task(run_every=(crontab(minute='*/1')), name="my_first_task")
def myfirsttask():
    print('this is my first task')


@shared_task()
def sleepy(duration):
    sleep(duration)
    return None


@shared_task()
def parseFromMechta():
    return parse()
