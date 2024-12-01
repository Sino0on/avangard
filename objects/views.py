from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *


class BuildingListApiView(generics.ListAPIView):
    serializer_class = BuildingListSerializer
    queryset = Building


class BuildingDetailApiView(generics.RetrieveAPIView):
    serializer_class = BuildingSerializer
    queryset = Building
    lookup_field = 'pk'

