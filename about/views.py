from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .models import AboutUs
from .serializers import AboutUsSerializer

class AboutUsView(GenericAPIView):
    serializer_class = AboutUsSerializer
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        about_us = AboutUs.load()  # Singleton ensures there's always one instance
        serializer = AboutUsSerializer(about_us)
        return Response(serializer.data)
