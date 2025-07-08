from rest_framework import serializers
from .models import HomeInfo, Address, AddressFooter


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['link', 'title']


class HomeInfoSerializer(serializers.ModelSerializer):
    address = AddressSerializer(many=True, source='addresses')

    class Meta:
        fields = '__all__'
        model = HomeInfo


class AddressFooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressFooter
        fields = ['link', 'title']
