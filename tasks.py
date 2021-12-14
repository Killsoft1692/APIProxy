import os
from bson.objectid import ObjectId

import requests
from celery import Celery
from pymongo import MongoClient, ASCENDING
from celery.schedules import crontab

import settings

celery = Celery('worker', broker=os.environ.get('BROKER_URL'))


celery.conf.beat_schedule = {
    'execute': {
        'task': 'tasks.execute',
        'schedule': crontab(hour='*/1'),  # execute each hour
    }
}


@celery.task
def execute():
    with MongoClient(os.environ.get('DB_URL')) as client:
        saved_requests = client.main['storage'].find({}).sort('added_at', ASCENDING).limit(settings.REQUESTS_LIMIT)
        for request in saved_requests:
            try:
                # Make request
                requests.get(f'https://{settings.REMOTE_HOST}/?{request.get("query_params")}')
                # Remove object after successful request
                client.main['storage'].delete_one({'_id': ObjectId(request.get('_id'))})
            except requests.RequestException:
                continue


