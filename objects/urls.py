from django.urls import path
from .views import *


urlpatterns = [
    path('list/', BuildingListApiView.as_view()),
    # path('list/3d/', ObjectsForHomeApiView.as_view()),
    path('list/3d/', ThreedListViewApi.as_view()),
    path('detail/<slug:slug>/', BuildingDetailApiView.as_view()),
    path('detail/3d/<int:id>/', ThreeDDetailApiView.as_view()),
    path('list/ended/', BuildingEndedApiView.as_view()),
    path('detail/ended/<slug:slug>/', BuildingEndedDetailApiView.as_view()),
    path('construction-progress/<int:building_id>/', ConstructionProgressApiView.as_view(),
         name='construction-progress'),
]
