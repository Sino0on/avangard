from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import *
from .serializers import *


class BuildingListApiView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = BuildingListSerializer
    queryset = Building.objects.all()


class BuildingDetailApiView(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = BuildingSerializer
    queryset = Building.objects.all()
    lookup_field = 'pk'

