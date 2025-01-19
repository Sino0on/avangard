from django.urls import path
from .views import *

urlpatterns = [
    path('list/', TenderListView.as_view(), name='tender-list'),
    path('detail/<int:id>/', TenderDetailView.as_view(), name='tender-detail'),
    path('create/application/<int:id>/', CreateTenderApplicationView.as_view(), name='application-create'),
]
