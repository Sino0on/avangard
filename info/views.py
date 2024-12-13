from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Contacts, TechnicalBase
from .serializers import ContactsSerializer, TechnicalBaseSerializer


class GetContactInfoApiView(APIView):
    permission_classes = [AllowAny]
    def get(self, request, *args, **kwargs):
        contact = Contacts.load()  # Загружаем единственный экземпляр Contacts
        serializer = ContactsSerializer(contact)
        return Response(serializer.data)


class TechnicalBaseApiView(APIView):
    permission_classes = [AllowAny]
    def get(self, request, *args, **kwargs):
        technical_base = TechnicalBase.load()  # Получаем единственную запись модели TechnicalBase
        serializer = TechnicalBaseSerializer(technical_base)
        return Response(serializer.data)