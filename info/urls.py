from django.urls import path
from .views import GetContactInfoApiView, TechnicalBaseApiView

urlpatterns = [
    path('contact-info/', GetContactInfoApiView.as_view(), name='get-contact-info'),
    path('technical-base/', TechnicalBaseApiView.as_view(), name='technical-base'),

]
