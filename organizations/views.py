from rest_framework import viewsets

from .models import Organizations
from .serializers import OrganizationsSer


class OrganizationsViewSet(viewsets.ModelViewSet):
    queryset = Organizations.objects.all()
    serializer_class = OrganizationsSer
