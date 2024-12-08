from rest_framework import serializers
from .models import *


class InterestingNearbySerializer(serializers.ModelSerializer):
    class Meta:
        model = InterestingNearby
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ArchitectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Architecture
        fields = '__all__'


class BlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlockInfo
        fields = '__all__'


class FloorSchemaSerializer(serializers.ModelSerializer):
    blocks = BlockSerializer(many=True)
    class Meta:
        model = FloorSchema
        fields = '__all__'


class AdvantageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advantage
        fields = '__all__'


class ImageGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageGallery
        fields = '__all__'


class InterestingNearbyBuildingSerializer(serializers.ModelSerializer):
    building = InterestingNearbySerializer()

    class Meta:
        model = InterestingNearbyBuilding
        fields = ['id', 'building']

class Section1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Section1
        fields = '__all__'

class Section2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Section2
        fields = '__all__'

class Section3Serializer(serializers.ModelSerializer):
    class Meta:
        model = Section3
        fields = '__all__'

class Section4Serializer(serializers.ModelSerializer):
    floorschemas = FloorSchemaSerializer(many=True)
    class Meta:
        model = Section4
        fields = '__all__'

class Section5Serializer(serializers.ModelSerializer):
    class Meta:
        model = Section5
        fields = '__all__'

class Section6Serializer(serializers.ModelSerializer):
    architecture = ArchitectureSerializer(many=True)
    class Meta:
        model = Section6
        fields = '__all__'

class Section7Serializer(serializers.ModelSerializer):
    images = ImageGallerySerializer(many=True)
    class Meta:
        model = Section7
        fields = '__all__'

class Section8Serializer(serializers.ModelSerializer):
    advantages = AdvantageSerializer(many=True)

    class Meta:
        model = Section8
        fields = '__all__'

class Section9Serializer(serializers.ModelSerializer):
    interest_nearby = InterestingNearbyBuildingSerializer(many=True)

    class Meta:
        model = Section9
        fields = '__all__'

class Section10Serializer(serializers.ModelSerializer):
    class Meta:
        model = Section10
        fields = '__all__'

class Section11Serializer(serializers.ModelSerializer):
    class Meta:
        model = Section11
        fields = '__all__'

class BuildingSerializer(serializers.ModelSerializer):
    section1 = Section1Serializer(source='section_1')
    section2 = Section2Serializer(source='section_2')
    section3 = Section3Serializer(source='section_3')
    section4 = Section4Serializer(source='section_4')
    section5 = Section5Serializer(source='section_5')
    section6 = Section6Serializer(source='section_6')
    section7 = Section7Serializer(source='section_7')
    section8 = Section8Serializer(source='section_8')
    section9 = Section9Serializer(source='section_9')
    section10 = Section10Serializer(source='section_10')
    section11 = Section11Serializer(source='section_11')

    class Meta:
        model = Building
        fields = '__all__'


class BuildingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = ['slug', 'title', 'banner']
