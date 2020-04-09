from rest_framework import viewsets
from rest_framework.response import Response
from .models import Services
from .serializers import ServicesSer
from .tasks import update_service


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
            update_service.apply_async((payload, ), queue="default")
            return Response("Queued", 201)
        except Exception as ex:
            return Response({"details": str(ex)}, 400)
