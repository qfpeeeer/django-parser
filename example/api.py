from .models import Data
from rest_framework import viewsets, permissions
from .serializers import DataSerializer


class DataViewSet(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = DataSerializer
