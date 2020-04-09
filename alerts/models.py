from django.db import models

from events.models import STATUS_CHOICES


class AlertsSettings(models.Model):
    status = models.IntegerField(choices=STATUS_CHOICES)
    delay = models.IntegerField(
        default=600, help_text="Time delay in seconds before sending the next alert message")
    channels = models.CharField(
        max_length=400, help_text="Channels list i.e comma separated")
    owner = models.ForeignKey(
        'auth.User', related_name='alerts_settings', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
