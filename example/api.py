from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Phone, Laptop, Monitor, Keyboard
from .models import PhoneHistory
from rest_framework import viewsets, permissions
from .serializers import CategorySerializer, PhoneSerializer, PhoneFullSerializer

from django.core import serializers


class PhoneViewSet(viewsets.ModelViewSet):
    queryset = Phone.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CategorySerializer


# class ProductView(APIView):
#     def gef(self, request, pk):
#         queryset = Phone.objects.all().filter(id=pk)
#         ProductSerializer(queryset, )
#         return Response
#

# class PhonesView(ListAPIView):
#     def get_queryset(self, pk):
#         return queryset = PhoneHistory.objects.all().filter(id=pk)
#     serializer_class = PhoneSerializer


class PhonesHistoryView (ListAPIView):
    serializer_class = PhoneFullSerializer

    def get_queryset(self):
        phone_id = self.kwargs['pk']
        queryset = Phone.objects.filter(id=phone_id)
        return queryset


class PhoneInfoView (ListAPIView):
    serializer_class = PhoneSerializer

    def get_queryset(self):
        phone_id = self.kwargs['pk']
        queryset = PhoneHistory.objects.filter(category_id=phone_id)
        return queryset


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
