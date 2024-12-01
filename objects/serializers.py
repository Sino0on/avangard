from rest_framework import serializers
from .models import *


class InterestingNearbySerializer(serializers.ModelSerializer):
    class Meta:
        model = InterestingNearby
        fields = '__all__'


class Categry(serializers.ModelSerializer):
    class Meta:
        model = Categry
        fields = '__all__'


class AdvantageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advantage
        fields = '__all__'


class InterestingNearbyBuildingSerializer(serializers.ModelSerializer):
    interesting_nearby = InterestingNearbySerializer()

    class Meta:
        model = InterestingNearbyBuilding
        fields = '__all__'


class BuildingSerializer(serializers.ModelSerializer):
    interetes_places = InterestingNearbyBuildingSerializer(source='interetes')

    class Meta:
        model = Building
        fields = '__all__'


class BuildingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = ['title', 'banner']
