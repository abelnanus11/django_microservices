from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    company = models.CharField(max_length=255)
    website_link = models.URLField(max_length=200, blank=True, null=True)
    posted_at = models.DateTimeField(auto_now_add=True)
