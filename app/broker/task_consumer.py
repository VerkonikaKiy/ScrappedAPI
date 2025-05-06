#Файл будет перемещен в проект скраппера
import json
import time
from rabbit_channel import RabbitChannel


def callback(ch, method, properties, body):
    with RabbitChannel('tasks') as task_channel:
        task_channel = task_channel.get_channel()
        result = json.loads(body)
        # Извлечение из "task" задач, обработка скраппером
        ch.basic_ack(delivery_tag=method.delivery_tag)
        print(f"Processed {result}")
        time.sleep(10)


if __name__ == '__main__':
    with RabbitChannel('tasks') as task_channel:
        queue = task_channel.queue
        tasks_channel = task_channel.get_channel()
        tasks_channel.basic_consume(queue=queue,
                                    on_message_callback=callback)
        print(' [*] Waiting for messages. To exit press CTRL+C')
        tasks_channel.start_consuming()
