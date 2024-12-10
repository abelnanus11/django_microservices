import pika
from rest_framework.viewsets import ModelViewSet
from .models import Job
from .serializers import JobSerializer

def publish_to_queue(message):
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue='job_post_queue')
    channel.basic_publish(exchange='', routing_key='job_post_queue', body=message)
    connection.close()

class JobViewSet(ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def perform_create(self, serializer):
        # Save the job and publish an event
        job = serializer.save()
        publish_to_queue(f"New job posted: {job.title}")
