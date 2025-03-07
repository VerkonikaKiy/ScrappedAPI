import json
import random
import time
import uuid
import pika

from rabbit_channel import RabbitChannel


def execute(task_id, channel):
    result = {}
    channel.basic_publish(exchange='', routing_key='results', body=json.dumps(result, indent=4))


def callback(ch, method, properties, body):
    with RabbitChannel('results') as results_channel:
        results_channel = results_channel.get_channel()
        task = json.loads(body)
        execute(task['uuid'], results_channel)
        ch.basic_ack(delivery_tag=method.delivery_tag)
        print(f"Processed {body}")
        time.sleep(10)


if __name__ == '__main__':
    with RabbitChannel('tasks') as tasks_channel:
        queue = tasks_channel.queue
        tasks_channel = tasks_channel.get_channel()
        tasks_channel.basic_consume(queue=queue,
                                    on_message_callback=callback)

        print(' [*] Waiting for messages. To exit press CTRL+C')
        tasks_channel.start_consuming()
