from django.urls import path
from .views import AboutUsView, ApplicationCreateView, MailingCreateView

urlpatterns = [
    path('about-us/', AboutUsView.as_view(), name='about-us'),
    path('application/create/', ApplicationCreateView.as_view(), name='application'),
    path('mailing/', MailingCreateView.as_view(), name='mailing'),
]
