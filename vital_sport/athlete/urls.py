from django.urls import path
from .views import *

app_name="athlete"

urlpatterns = [
    path('add/', AthleteCreate.as_view(), name='athletes_add'),
    path('', AthleteAll.as_view(), name='athletes'),
    path('<str:athlete_id>/', AthleteCRUD.as_view(), name='athletes_detail'),
    path('<str:athlete_id>/update/', AthleteCRUD.as_view(), name='athletes_update'),
    path('<str:athlete_id>/delete/', AthleteCRUD.as_view(), name='athletes_delete'),
]