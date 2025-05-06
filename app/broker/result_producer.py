import pika
# from fastapi import Depends
# from sqlalchemy.orm import Session
# from sqlalchemy.testing import db
import json

# from api.tasks.task_repository import TaskRepository
from broker.rabbit_channel import RabbitChannel
# from models.database import get_db


def get_result():
    result = "sdLKBJZMLDbrGWJ"
    res = json.dumps(result)
    print(res)
    return res


def producer():
    with RabbitChannel('results') as result_channel:
        queue = result_channel.queue
        task = get_result()
        result_channel = result_channel.get_channel()
        result_channel.basic_publish(exchange="",
            routing_key="results",
            body=task)
        print('Message sent')


if __name__ == "__main__":
    producer()