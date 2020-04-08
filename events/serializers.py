from rest_framework import serializers

from .models import Events, Incidents


class EventsSer(serializers.ModelSerializer):
    duration = serializers.DecimalField(max_digits=11, decimal_places=2)
    date_time = serializers.DateTimeField()

    class Meta:
        model = Events
        fields = "__all__"


class IncidentsSer(serializers.ModelSerializer):
    class Meta:
        model = Incidents
        fields = "__all__"
