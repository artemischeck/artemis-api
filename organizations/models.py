from django.db import models


class Organizations(models.Model):
    name = models.CharField(max_length=140)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=70)
    address = models.CharField(max_length=200, blank=True, null=True)
    country = models.CharField(max_length=2)

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
