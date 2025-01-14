from django.http import Http404
from django.shortcuts import render
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema, extend_schema_view
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny
from unicodedata import category
from yaml import safe_load

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
        category_id = self.request.GET.get('category_id')
        slug = self.kwargs.get('slug')
        if category_id:
            queryset = Building.objects.filter(slug=slug, category__id=category_id)
        else:
            queryset = Building.objects.filter(slug=slug)
        if not queryset.exists():
            raise Http404("Категория не существует")
        return queryset

@extend_schema_view(
    get=extend_schema(
        description='Категория айди',
        summary='вфыефт',
        parameters=[
            OpenApiParameter(name='category_id',
                             description='ID Категория',
                             type=OpenApiTypes.INT, required=True),
        ]
    ),
)
class BuildingEndedApiView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = BuildingListSerializer
    queryset = Building.objects.filter(status='ended')

    def get_queryset(self):
        category_id = self.request.GET.get('category_id')
        if category_id:
            queryset = Building.objects.filter(status='ended', category__id=category_id)
        else:
            queryset = Building.objects.filter(status='ended')
        if not queryset.exists():
            raise Http404("Категория не существует")
        return queryset


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



class ConstructionProgressApiView(generics.ListAPIView):
    serializer_class = ConstructionProgressSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        """
        Возвращает список ConstructionProgress, связанных с конкретным Building.
        """
        building_id = self.kwargs.get('building_id')
        return ConstructionProgress.objects.filter(building_id=building_id)


class ObjectsForHomeApiView(generics.ListAPIView):
    serializer_class = ObjectsForHomeSerializer
    permission_classes = [AllowAny]
