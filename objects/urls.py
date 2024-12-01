from django.urls import path
from .views import *


urlpatterns = [
    path('list/', BuildingListApiView.as_view()),
    path('detail/<int:pk>/', BuildingDetailApiView.as_view())
]
