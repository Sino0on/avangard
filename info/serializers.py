from rest_framework import serializers
from .models import Contacts, SalesOffice, RequisitesInSom, RequisitesInDollar, TechnicalBaseImage, TechnicalBase


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

class ContactsSerializer(serializers.ModelSerializer):
    sales_offices = SalesOfficeSerializer(many=True, read_only=True)
    som_requisites = RequisitesInSomSerializer(many=True, read_only=True)
    dollar_requisites = RequisitesInDollarSerializer(many=True, read_only=True)

    class Meta:
        model = Contacts
        fields = ['addresses', 'requisites', 'sales_offices', 'som_requisites', 'dollar_requisites']

class TechnicalBaseImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechnicalBaseImage
        fields = ['image']

class TechnicalBaseSerializer(serializers.ModelSerializer):
    images = TechnicalBaseImageSerializer(many=True, read_only=True)

    class Meta:
        model = TechnicalBase
        fields = ['title', 'description', 'youtube_url', 'images']