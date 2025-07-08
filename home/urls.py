from django.urls import path
from .views import GetHomeInfoApi, GetAddressesFooter

urlpatterns = [
    path('home-info', GetHomeInfoApi.as_view()),
    path('footer', GetAddressesFooter.as_view())
]
