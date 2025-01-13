import pika
import os
import sys

class mqProducer(mqProducerInterface):
    def __init__(self, routing_key: str, exchange_name: str) -> None:
        self.routing_key = routing_key
        self.exchange_name = exchange_name
        self.setupRMQConnection()
        self.conParams = None
        self.channel = None
        self.connection = None
        self.channel = None

    def setupRMQConnection(self) -> None:
        # Set-up Connection to RabbitMQ service
        self.conParams = pika.URLParameters(os.environ['AMQP_URL'])
        self.connection = pika.BlockingConnection(parameters=self.conParams)
        # Establish Channel
        self.channel = self.connection.channel()
        # Create the exchange if not already present
        self.channel.exchange_declare(self.exchange_name)


    def publishOrder(self, message: str) -> None:
        # Basic Publish to Exchange
        self.channel.basic_publish(message)
        # Close Channel
        self.channel.close()
        # Close Connection
        self.connection.close()


