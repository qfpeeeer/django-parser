from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Phone, Laptop, Monitor, Keyboard
from .models import PhoneHistory
from rest_framework import viewsets, permissions
from .serializers import CategorySerializer, ProductSerializer


class PhoneViewSet(viewsets.ModelViewSet):
    queryset = Phone.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CategorySerializer


class PhonesView(APIView):
    def get (self, request, pk):
        snippet = PhoneHistory.objects.get(id=pk)
        serializer = ProductSerializer (snippet)
        return Response(serializer.data)


class LaptopViewSet(viewsets.ModelViewSet):
    queryset = Laptop.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CategorySerializer


class MonitorViewSet(viewsets.ModelViewSet):
    queryset = Monitor.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CategorySerializer


class KeyboardViewSet(viewsets.ModelViewSet):
    queryset = Keyboard.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CategorySerializer
