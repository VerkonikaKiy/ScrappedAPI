import json
import random
import time
import uuid
import pika

from broker.rabbit_channel import RabbitChannel


def execute(task_id, channel):
    result = {}
    channel.basic_publish(exchange='', routing_key='results', body=json.dumps(result, indent=4))


def callback(ch, method, properties, body):
    with RabbitChannel('results') as results_channel:
        results_channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
        print(" [x] Sent 'Hello World!'")
        results_channel = results_channel.get_channel()
        task = json.loads(body)
        execute(task['uuid'], results_channel)
        print(f"Processed {body}")
        time.sleep(10)
        