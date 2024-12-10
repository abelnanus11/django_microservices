from django.core.management.base import BaseCommand
from search.consumers import consume_jobs

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        consume_jobs()
