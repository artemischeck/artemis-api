from rest_framework import serializers

from .models import Events, Incidents


class EventsSer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = "__all__"


class IncidentsSer(serializers.ModelSerializer):
    class Meta:
        model = Incidents
        fields = "__all__"
