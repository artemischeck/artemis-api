from django.db import models


class Events(models.Model):
    # Capture events in time series
    service = models.CharField(max_length=140)
    status = models.BooleanField(default=False)
    host = models.CharField(max_length=140)
    tags = models.CharField(max_length=400, blank=True, null=True)
    request = models.TextField(blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    duration = models.DecimalField(max_digits=11, decimal_places=2)
    date_time = models.DateTimeField()
    incident = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)


class Incidents(models.Model):
    # Issues captured based on events
    event = models.ForeignKey(
        Events, related_name='incidents', on_delete=models.CASCADE)
    resolved = models.BooleanField(default=False)
    threshold = models.IntegerField(default=1)

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
