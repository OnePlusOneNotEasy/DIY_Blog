from django.db import models
from django.urls import reverse

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def get_html_url(self):
        url = reverse('calendar:calendar_update', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'
