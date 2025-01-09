from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .serializers import *
from .models import *
from rest_framework import generics


class GetHomeInfoApi(generics.GenericAPIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        contact = HomeInfo.load()  # Загружаем единственный экземпляр Contacts
        serializer = HomeInfoSerializer(contact)
        return Response(serializer.data)

