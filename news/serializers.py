from rest_framework import serializers
from .models import News, NewsImages, LinkNews


class NewsImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsImages
        fields = ['image']


class NewsSerializer(serializers.ModelSerializer):
    main_image = serializers.ImageField()
    created_at = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = ['main_image', 'slug', 'title', 'created_at']

    def get_created_at(self, obj):
        # Преобразование даты в формат ДД.ММ.ГГГГ
        return obj.created_at.strftime('%d.%m.%Y')

class NewsDetailSerializer(serializers.ModelSerializer):
    main_image = serializers.ImageField()
    news_images = NewsImagesSerializer(many=True, read_only=True)

    class Meta:
        model = News
        fields = ['title', 'description', 'youtube_link', 'main_image', 'created_at', 'slug', 'news_images']


class LinkNewsSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()
    created_at = serializers.SerializerMethodField()

    class Meta:
        model = LinkNews
        fields = ['title', 'url', 'image', 'created_at']

    def get_created_at(self, obj):
        # Преобразование даты в формат ДД.ММ.ГГГГ
        return obj.created_at.strftime('%d.%m.%Y')