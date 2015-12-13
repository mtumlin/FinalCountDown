from django.db import models


class Event(models.Model):
    heading_text = models.CharField(max_length=200)
    date = models.DateTimeField('Event Date')

    date.admin_order_field = 'date'

    def __str__(self):
        return self.heading_text