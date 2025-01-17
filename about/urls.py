from django.urls import path
from .views import AboutUsView, ApplicationCreateView

urlpatterns = [
    path('about-us/', AboutUsView.as_view(), name='about-us'),
    path('application/create/', ApplicationCreateView.as_view(), name='application'),
]
