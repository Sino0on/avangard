from rest_framework import serializers
from .models import *


class RequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requirement
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = '__all__'


class TenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tender
        fields = ['id', 'title', 'mini_description', 'created_at', 'place']


class TenderDetailSerializer(serializers.ModelSerializer):
    more_info = RequirementSerializer(many=True, read_only=True, source='requers')
    contacts = ContactSerializer(many=True, read_only=True, source='contacts_tender')

    class Meta:
        model = Tender
        fields = '__all__'


class TenderApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TenderApplication
        fields = [
            'id', 'company_name', 'inn', 'yur_address', 'email',
            'phone_number', 'theme', 'comment', 'comment_file', 'created_at'
        ]


class VacanciSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancies
        fields = '__all__'


class VacanciApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = VacanciApplication
        fields = '__all__'
