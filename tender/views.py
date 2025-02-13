from django.shortcuts import render
from rest_framework.generics import get_object_or_404, GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import *
from rest_framework import generics
from .serializers import *
from rest_framework import generics, serializers, status


class TenderListView(generics.ListAPIView):
    queryset = Tender.objects.all()
    serializer_class = TenderSerializer
    permission_classes = [AllowAny]


class TenderDetailView(generics.RetrieveAPIView):
    queryset = Tender.objects.all()
    serializer_class = TenderDetailSerializer
    permission_classes = [AllowAny]
    lookup_field = 'id'


class CreateTenderApplicationView(generics.GenericAPIView):
    serializer_class = TenderApplicationSerializer
    permission_classes = [AllowAny]

    def post(self, request, id):
        tender = get_object_or_404(pk=id)
        serializer = TenderApplicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(tender=tender)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VacanciView(GenericAPIView):
    serializer_class = VacanciSerializer
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        about_us = Vacancies.load()  # Singleton ensures there's always one instance
        serializer = VacanciSerializer(about_us, context={'request': request})
        return Response(serializer.data)


class VacanciApplicationView(generics.CreateAPIView):
    serializer_class = VacanciApplication
    permission_classes = [AllowAny]