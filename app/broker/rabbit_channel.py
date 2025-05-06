import os

import pika


class RabbitChannel(object):
    def __init__(self, queue):
        self.queue = queue

    def __enter__(self):
        # TODO: get credentials from config
        self.parameters = pika.ConnectionParameters(host='localhost',
                                       port=5672,
                                       virtual_host='/',
                                       credentials=pika.PlainCredentials(
                                           username=os.getenv('rabbit_username'),
                                           password=os.getenv('rabbit_password')
                                           #  username = 'guest1',
                                           #  password = '1k68JQcQ'
                                       )
                                       )
        self.connection = pika.BlockingConnection(self.parameters)
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.queue, durable=True)
        self.channel.basic_qos(prefetch_count=1)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()

    def get_channel(self):
        return self.channel


