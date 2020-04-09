from rest_framework import viewsets
from rest_framework.response import Response
import json

from .models import Services
from .serializers import ServicesSer


class ServicesViewSet(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServicesSer

    def get_queryset(self):
        return Services.objects.filter(owner=self.request.user)

    def create(self, request):
        """
        Register a new service event
        """
        try:
            payload = request.data
            service, _ = Services.objects.update_or_create(
                owner=request.user,
                label=payload.get('label'),
                host=payload.get('host'),
                defaults={
                    'tags': payload.get('tags'),
                    'message': payload.get('message'),
                    'duration': payload.get('duration'),
                    'date_time': payload.get('date_time'),
                }
            )
            resp = ServicesSer(service, many=False).data
            return Response(resp, 201)
        except Exception as ex:
            return Response({"details": str(ex)}, 400)
