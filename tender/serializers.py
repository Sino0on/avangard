from rest_framework import serializers
from .models import *


class MoreInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoreInfo
        fields = ['id', 'title', 'link', 'file']


class TenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tender
        fields = ['id', 'title', 'mini_description', 'created_at']


class TenderDetailSerializer(serializers.ModelSerializer):
    more_info = MoreInfoSerializer(many=True, read_only=True, source='more_infos')

    class Meta:
        model = Tender
        fields = ['id', 'title', 'mini_description', 'description', 'created_at', 'more_info']


class TenderApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TenderApplication
        fields = [
            'id', 'company_name', 'inn', 'yur_address', 'email',
            'phone_number', 'theme', 'comment', 'comment_file', 'created_at'
        ]

