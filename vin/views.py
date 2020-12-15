from vin.models import Vin
from rest_framework import viewsets
from rest_framework import permissions
from vin.serializer import VinSerializer


class VinViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Vin.objects.all()
    serializer_class = VinSerializer
    permission_classes = [permissions.IsAuthenticated]