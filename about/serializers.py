from rest_framework import serializers
from .models import AboutUs, Section1, Section2, Section3, Section4, Section5, Section6, Materials, Gramota, Licence, \
    Sertificat, Application


class MaterialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materials
        fields = ['id', 'title', 'section']

class GramotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gramota
        fields = ['id', 'title', 'image', 'section']

class LicenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Licence
        fields = ['id', 'title', 'image', 'section']

class SertificatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sertificat
        fields = ['id', 'title', 'image', 'section']

class Section1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Section1
        fields = ['id', 'title', 'description', 'about_us']

class Section2Serializer(serializers.ModelSerializer):
    materials = MaterialsSerializer(many=True, read_only=True, source='materials_set')

    class Meta:
        model = Section2
        fields = ['id', 'title', 'description', 'about_us', 'materials']

class Section3Serializer(serializers.ModelSerializer):
    class Meta:
        model = Section3
        fields = ['id', 'title', 'description', 'about_us']

class Section4Serializer(serializers.ModelSerializer):
    gramotas = GramotaSerializer(many=True, read_only=True, source='gramota_set')

    class Meta:
        model = Section4
        fields = ['id', 'title', 'description', 'about_us', 'gramotas']

class Section5Serializer(serializers.ModelSerializer):
    licences = LicenceSerializer(many=True, read_only=True, source='licence_set')

    class Meta:
        model = Section5
        fields = ['id', 'title', 'description', 'about_us', 'licences']

class Section6Serializer(serializers.ModelSerializer):
    sertificats = SertificatSerializer(many=True, read_only=True, source='sertificat_set')

    class Meta:
        model = Section6
        fields = ['id', 'title', 'description', 'about_us', 'sertificats']

class AboutUsSerializer(serializers.ModelSerializer):
    section_1 = Section1Serializer()
    section_2 = Section2Serializer()
    section_3 = Section3Serializer()
    section_4 = Section4Serializer()
    section_5 = Section5Serializer()
    section_6 = Section6Serializer()

    class Meta:
        model = AboutUs
        fields = [
            'description',
            'advantages',
            'youtube_url_1',
            'youtube_url_2',
            'section_1',
            'section_2',
            'section_3',
            'section_4',
            'section_5',
            'section_6',
        ]


# Сериализатор для модели Application
class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['id', 'theme', 'name', 'phone', 'email', 'created_at', 'comment']
        read_only_fields = ['created_at']