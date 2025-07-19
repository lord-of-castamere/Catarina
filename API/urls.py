# tu_app/urls.py

# ---------------------------------------------------------------------------- #

from .views import *
from django.urls import path

# ---------------------------------------------------------------------------- #

app_name = 'api'

urlpatterns = [
    path('activities/completed/', ActivityActiveListView.as_view(), name='CompletedActivities'),
    path('activities/pending/', ActivityInactiveListView.as_view(), name='PendingActivities'),
    path('activities/list/', ActivityListView.as_view(), name='ActivitiesList'),
    path('activities/create/', ActivityCreateView.as_view(), name='ActivityCreate'),
    path('activities/<int:pk>/', ActivityRetrieveUpdateDestroyView.as_view(), name='ActivitiesCRUD'),
]

# ---------------------------------------------------------------------------- #
