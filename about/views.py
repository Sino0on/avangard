from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .models import AboutUs
from .serializers import AboutUsSerializer, ApplicationSerializer, MailingSerializer


class AboutUsView(GenericAPIView):
    serializer_class = AboutUsSerializer
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        about_us = AboutUs.load()  # Singleton ensures there's always one instance
        serializer = AboutUsSerializer(about_us)
        return Response(serializer.data)


# Вьюшка для создания заявки
class ApplicationCreateView(GenericAPIView):
    permission_classes = [AllowAny]  # Разрешить доступ всем
    serializer_class = ApplicationSerializer

    def post(self, request, *args, **kwargs):
        serializer = ApplicationSerializer(data=request.data)
        if serializer.is_valid():
            application = serializer.save()
            return Response({
                "success": True,
                "message": "Заявка успешно создана!",
                "application": ApplicationSerializer(application).data
            }, status=201)
        return Response({
            "success": False,
            "errors": serializer.errors
        }, status=400)


class MailingCreateView(GenericAPIView):
    permission_classes = [AllowAny]  # Разрешить доступ всем
    serializer_class = MailingSerializer

    def post(self, request, *args, **kwargs):
        serializer = MailingSerializer(data=request.data)
        if serializer.is_valid():
            application = serializer.save()
            return Response({
                "success": True,
                "message": "Заявка успешно создана!",
                "application": MailingSerializer(application).data
            }, status=201)
        return Response({
            "success": False,
            "errors": serializer.errors
        }, status=400)
