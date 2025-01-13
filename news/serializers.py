from rest_framework import serializers
from .models import News, NewsImages, LinkNews


class NewsImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsImages
        fields = ['image']


class NewsSerializer(serializers.ModelSerializer):
    main_image = serializers.ImageField()

    class Meta:
        model = News
        fields = ['main_image', 'slug', 'title', 'created_at']


class NewsDetailSerializer(serializers.ModelSerializer):
    main_image = serializers.ImageField()
    news_images = NewsImagesSerializer(many=True, read_only=True)

    class Meta:
        model = News
        fields = ['title', 'description', 'youtube_link', 'main_image', 'created_at', 'slug', 'news_images']


class LinkNewsSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()

    class Meta:
        model = LinkNews
        fields = ['title', 'url', 'image', 'created_at']
