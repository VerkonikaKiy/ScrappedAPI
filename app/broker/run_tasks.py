import json
import uuid

from rabbit_channel import RabbitChannel

with RabbitChannel('tasks') as tasks_channel:
    tasks_channel = tasks_channel.get_channel()
    task = {}
    tasks_channel.basic_publish(exchange='', routing_key='tasks', body=json.dumps(task, indent=4))
