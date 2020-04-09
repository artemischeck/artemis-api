from django.db import models

STATUS_CHOICES = (
    (1, "UP"),
    (2, "WARN"),
    (3, "SLOW"),
    (4, "DOWN"),
    (5, "OFF"),
)


class Services(models.Model):
    label = models.CharField(max_length=140)
    status = models.IntegerField(choices=STATUS_CHOICES)
    host = models.CharField(max_length=140)
    tags = models.CharField(max_length=400, blank=True, null=True)
    message = models.TextField(
        blank=True, null=True, help_text="Status summary")
    duration = models.DecimalField(max_digits=11, decimal_places=4)
    date_time = models.DateTimeField(help_text="Actual captured date time")

    owner = models.ForeignKey(
        'auth.User', related_name='services', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        ordering = ('-status', '-date_time')
        unique_together = ('label', 'host', 'owner')
