from rest_framework import serializers
from .models import HomeInfo


class HomeInfoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = HomeInfo
