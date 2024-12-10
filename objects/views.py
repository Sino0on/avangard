from django.http import Http404
from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import *
from .serializers import *


class BuildingListApiView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = BuildingListSerializer
    queryset = Building.objects.filter(status='active')


class BuildingDetailApiView(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = BuildingSerializer
    queryset = Building.objects.all()
    lookup_field = 'slug'

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        queryset = Building.objects.filter(slug=slug)
        if not queryset.exists():
            raise Http404("Категория не существует")
        return queryset


class BuildingEndedApiView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = BuildingListSerializer
    queryset = Building.objects.filter(status='ended')


class BuildingEndedDetailApiView(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = BuildingEndedSerializer
    queryset = Building.objects.all()
    lookup_field = 'slug'

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        queryset = Building.objects.filter(slug=slug)
        if not queryset.exists():
            raise Http404("Категория не существует")
        return queryset