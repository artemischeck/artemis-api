from rest_framework import viewsets
from rest_framework.response import Response
import json

from .models import Events, Incidents
from .serializers import EventsSer, IncidentsSer


class EventsViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventsSer

    # def create(self, request):
    #     print(json.dumps(request.data))
    #     return Response("ok")


class IncidentsViewSet(viewsets.ModelViewSet):
    queryset = Incidents.objects.all()
    serializer_class = IncidentsSer