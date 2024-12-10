import pika
import json
from .models import Job

def consume_jobs():
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue='job_post_queue')

    def callback(ch, method, properties, body):
        job_data = json.loads(body)
        Job.objects.create(**job_data)

    channel.basic_consume(queue='job_post_queue', on_message_callback=callback, auto_ack=True)
    print("Waiting for messages...")
    channel.start_consuming()
