# tu_app/urls.py

# ---------------------------------------------------------------------------- #

from .views import *
from django.urls import path

# ---------------------------------------------------------------------------- #

app_name = 'api'

urlpatterns = [
    path('users/', UserListView.as_view(), name='UsersList'),

    path('activities/', ActivityListCreateView.as_view(), name='ActivitiesListCreate'),
    path('activities/<int:pk>/', ActivityRetrieveUpdateDestroyView.as_view(), name='ActivitiesCRUD'),

    path('activities/completed/', ActivityActiveListView.as_view(), name='CompletedActivities'),
    path('activities/pending/', ActivityInactiveListView.as_view(), name='PendingActivities'),
]

# ---------------------------------------------------------------------------- #
