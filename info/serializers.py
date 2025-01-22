from rest_framework import serializers

from home.serializers import AddressSerializer
from .models import *


class SalesOfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesOffice
        fields = ['name', 'description']

class RequisitesInSomSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequisitesInSom
        fields = ['title', 'description']

class RequisitesInDollarSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequisitesInDollar
        fields = ['title', 'description']


class AddressesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class ContactsSerializer(serializers.ModelSerializer):
    sales_offices = SalesOfficeSerializer(many=True, read_only=True)
    som_requisites = RequisitesInSomSerializer(many=True, read_only=True)
    dollar_requisites = RequisitesInDollarSerializer(many=True, read_only=True)
    home_addresses = AddressSerializer(many=True, source='addresss')
    addresses = AddressesSerializer(many=True, read_only=True, source='addresses')

    class Meta:
        model = Contacts
        fields = "__all__"


class TechnicalBaseImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechnicalBaseImage
        fields = ['image']

class TechnicalBaseSerializer(serializers.ModelSerializer):
    images = TechnicalBaseImageSerializer(many=True, read_only=True)

    class Meta:
        model = TechnicalBase
        fields = ['title', 'description', 'youtube_url', 'images']