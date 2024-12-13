from django.urls import path
from .views import NewsListApiView, NewsDetailApiView, LinkNewsListApiView

urlpatterns = [
    path('news/', NewsListApiView.as_view(), name='news-list'),
    path('news/<slug:slug>/', NewsDetailApiView.as_view(), name='news-detail'),
    path('link-news/', LinkNewsListApiView.as_view(), name='link-news-list'),
]
