
# ---------------------------------------------------------------------------- #

from .views import *
from django.urls import path

# ---------------------------------------------------------------------------- #

app_name = 'Solaire'

urlpatterns = [
    path('', ListActivities.as_view(), name='ListActivities'),
    path('activities/<int:pk>/', DetailActivities.as_view(), name='DetailActivities'),
    path('activities/create/', CreateActivities.as_view(), name='CreateActivities'),
    path('activities/update/<int:pk>/', UpdateActivities.as_view(), name='UpdateActivities'),
    path('activities/delete/<int:pk>/', DeleteActivities.as_view(), name='DeleteActivities'),




]

# ---------------------------------------------------------------------------- #
