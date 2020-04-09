from rest_framework import viewsets
from rest_framework.response import Response
import json
from decimal import Decimal
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
            duration = payload.get('duration')
            if duration:
                duration = Decimal((payload.get('duration')/(10**9)))
            service, _ = Services.objects.update_or_create(
                owner=request.user,
                label=payload.get('label'),
                host=payload.get('host'),
                defaults={
                    'status': payload.get('status'),
                    'tags': payload.get('tags'),
                    'message': payload.get('message'),
                    'duration': duration,
                    'date_time': payload.get('date_time'),
                }
            )

            resp = ServicesSer(service, many=False).data
            return Response(resp, 201)
        except Exception as ex:
            print(ex)
            return Response({"details": str(ex)}, 400)
