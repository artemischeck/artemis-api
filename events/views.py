from rest_framework import viewsets

from .models import Events, Incidents
from .serializers import EventsSer, IncidentsSer


class EventsViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventsSer


class IncidentsViewSet(viewsets.ModelViewSet):
    queryset = Incidents.objects.all()
    serializer_class = IncidentsSer