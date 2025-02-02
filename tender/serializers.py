from rest_framework import serializers
from .models import *


class MoreInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoreInfo
        fields = ['id', 'title', 'link', 'file']


class TenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tender
        fields = ['id', 'title', 'mini_description', 'created_at', 'place']


class TenderDetailSerializer(serializers.ModelSerializer):
    more_info = MoreInfoSerializer(many=True, read_only=True, source='more_infos')

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
