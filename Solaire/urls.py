
# ---------------------------------------------------------------------------- #

from .views import *
from django.urls import path

# ---------------------------------------------------------------------------- #

app_name = 'Solaire'

urlpatterns = [
    path('', ListActivities.as_view(), name='ListActivities'),
    path('activities/completed/', ListCompletedActivities.as_view(), name='ListCompleted'),
    path('activities/pending/', ListPendingActivities.as_view(), name='ListPending'),
    path('activities/create/', CreateActivities.as_view(), name='CreateActivities'),
    path('activities/update/<int:pk>/', UpdateActivities.as_view(), name='UpdateActivities'),
    path('activities/delete/<int:pk>/', DeleteActivities.as_view(), name='DeleteActivities'),
]

# ---------------------------------------------------------------------------- #
