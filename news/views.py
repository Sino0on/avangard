from rest_framework import generics
from rest_framework.permissions import AllowAny

from utils.pagination import MyCustomPagination
from .models import News, LinkNews
from .serializers import NewsSerializer, NewsDetailSerializer, LinkNewsSerializer


class NewsListApiView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    pagination_class = MyCustomPagination
    permission_classes = [AllowAny]

class NewsDetailApiView(generics.RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsDetailSerializer
    lookup_field = 'slug'
    permission_classes = [AllowAny]


class LinkNewsListApiView(generics.ListAPIView):
    queryset = LinkNews.objects.all()
    serializer_class = LinkNewsSerializer
    pagination_class = MyCustomPagination
    permission_classes = [AllowAny]