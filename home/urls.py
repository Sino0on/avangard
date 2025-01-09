from django.urls import path
from .views import GetHomeInfoApi


urlpatterns = [
    path('home-info', GetHomeInfoApi.as_view())
]
