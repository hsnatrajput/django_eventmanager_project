from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    title = models.CharField(max_length=200, help_text="The title of the event.")
    description = models.TextField(help_text="A detailed description of the event.")
    date = models.DateField(help_text="The date of the event.")
    time = models.TimeField(help_text="The start time of the event.")
    organizer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='organized_events', help_text="The user or organization that is organizing the event.")
    attendees = models.ManyToManyField(User, blank=True, related_name='attending_events', help_text="Users who have registered or are attending the event.")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Timestamp for when the event was created.")
    updated_at = models.DateTimeField(auto_now=True, help_text="Timestamp for when the event was last updated.")

    def __str__(self):
        return self.title

 