from rest_framework import serializers

from .models import Services


class ServicesSer(serializers.ModelSerializer):
    duration = serializers.DecimalField(max_digits=11, decimal_places=4)
    date_time = serializers.DateTimeField()

    class Meta:
        model = Services
        fields = "__all__"