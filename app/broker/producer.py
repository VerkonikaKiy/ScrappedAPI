import json
from fastapi.encoders import jsonable_encoder
from app.api.tasks.task_repository import TaskRepository
from broker.rabbit_channel import RabbitChannel


def get_task():
    raw_task = TaskRepository.get_task_by_status('not_started')
    task = jsonable_encoder(raw_task)
    return task


def producer():
    with RabbitChannel('tasks') as task_channel:
        queue = task_channel.queue
        try:
            tasks = get_task()
            for task in tasks:
                tasks_channel = task_channel.get_channel()
                tasks_channel.basic_publish(exchange="",
                    routing_key="tasks",
                    body=json.dumps(task, indent=4))
                new_task = TaskRepository.change_task_status(task['uuid'], 'sent_to_execute')
                print('Message sent')
            for task in tasks:
                print(task)
                tasks_channel = task_channel.get_channel()
                tasks_channel.basic_publish(exchange="",
                    routing_key="tasks",
                    body=json.dumps(task, indent=4))
                print('Message sent')
        except IndexError:
            print('No tasks with status "not_started"')


if __name__ == "__main__":
    producer()
