from rest_framework import serializers
from .models import *


class ThreeDSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = ThreeD

class InterestingNearbySerializer(serializers.ModelSerializer):
    class Meta:
        model = InterestingNearby
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class FeaturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Features
        fields = '__all__'


class ArchitectureSerializer(serializers.ModelSerializer):
    features = FeaturesSerializer(many=True, source='Architecture_blocks')

    class Meta:
        model = Architecture
        fields = '__all__'


class BlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlockInfo
        fields = '__all__'


class FloorSchemaSerializer(serializers.ModelSerializer):
    blocks = BlockSerializer(many=True, source='floorschema_blocks')
    class Meta:
        model = FloorSchema
        fields = '__all__'


class AdvantageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advantage
        fields = '__all__'


class ParkingImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingImages
        fields = '__all__'


class ImageGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageGallery
        fields = '__all__'


class ApartmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartments
        fields = '__all__'


class InterestingNearbyBuildingSerializer(serializers.ModelSerializer):
    building = InterestingNearbySerializer()

    class Meta:
        model = InterestingNearbyBuilding
        fields = ['id', 'building', 'time']


class Section1Serializer(serializers.ModelSerializer):
    apartments = ApartmentsSerializer(many=True, source='Apartments_blocks')
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
    floorschemas = FloorSchemaSerializer(many=True, source='section_floors')
    class Meta:
        model = Section4
        fields = '__all__'


class Section5Serializer(serializers.ModelSerializer):
    images = ParkingImagesSerializer(many=True, source='ParkingImages_blocks')
    class Meta:
        model = Section5
        fields = '__all__'


class Section6Serializer(serializers.ModelSerializer):
    architecture = ArchitectureSerializer(many=True, source='Architecture_blocks')
    class Meta:
        model = Section6
        fields = '__all__'


class Section7Serializer(serializers.ModelSerializer):
    images = ImageGallerySerializer(many=True, source='section_images')

    class Meta:
        model = Section7
        fields = '__all__'

class Section8Serializer(serializers.ModelSerializer):
    advantages = AdvantageSerializer(many=True)

    class Meta:
        model = Section8
        fields = '__all__'

class Section9Serializer(serializers.ModelSerializer):
    interest_nearby = InterestingNearbyBuildingSerializer(many=True, source='interesteds_secrion')

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


class Section12Serializer(serializers.ModelSerializer):
    class Meta:
        model = Section12
        fields = '__all__'


class BuildingSerializer(serializers.ModelSerializer):
    about_complex = Section1Serializer(source='section_1')
    threed = ThreeDSerializer(source='threedes', many=True)
    object_metrics = Section2Serializer(source='section_2')
    before_after = Section3Serializer(source='section_3')
    floor_plans = Section4Serializer(source='section_4')
    parking_plan = Section5Serializer(source='section_5')
    architecture = Section6Serializer(source='section_6')
    gallery = Section7Serializer(source='section_7')
    advantages = Section8Serializer(source='section_8')
    interest_nearby = Section9Serializer(source='section_9')
    location = Section10Serializer(source='section_10')
    footer = Section11Serializer(source='section_11')
    numeration = Section12Serializer(source='section_12')

    class Meta:
        model = Building
        fields = '__all__'


class BuildingListSerializer(serializers.ModelSerializer):
    info = Section1Serializer(source='section_1')

    class Meta:
        model = Building
        fields = ['slug', 'title', 'imagepng', 'imagebg', 'info', 'mini_title', 'is_new', 'banner_img']


class BuildingEndedSerializer(serializers.ModelSerializer):
    section1 = Section1Serializer(source='section_1')
    section7 = Section7Serializer(source='section_7')

    class Meta:
        model = Building
        fields = ['title', 'mini_title', 'slug', 'section7', 'section1']


class ConstructionProgressImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConstructionProgressImage
        fields = ['image']

class ConstructionProgressSerializer(serializers.ModelSerializer):
    images = ConstructionProgressImageSerializer(many=True, read_only=True)

    class Meta:
        model = ConstructionProgress
        fields = ['id', 'month', 'year', 'images']


class ObjectsForHomeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['title', 'slug', 'threed']
        model = Building

