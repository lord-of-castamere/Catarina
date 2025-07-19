
# ---------------------------------------------------------------------------- #

from .serializers import *
from rest_framework import generics
from Solaire.models import Activities
from django.contrib.auth.models import User

# ---------------------------------------------------------------------------- #

class ActivityActiveListView(generics.ListAPIView):
    queryset = Activities.objects.filter(status=True)
    serializer_class = ActivitiesListSerializer

class ActivityInactiveListView(generics.ListAPIView):
    queryset = Activities.objects.filter(status=False)
    serializer_class = ActivitiesListSerializer

# ---------------------------------------------------------------------------- #

class ActivityListView(generics.ListAPIView):
    queryset = Activities.objects.all()
    serializer_class = ActivitiesListSerializer

class ActivityCreateView(generics.CreateAPIView):
    queryset = Activities.objects.all()
    serializer_class = ActivitiesSerializer

# ---------------------------------------------------------------------------- #

class ActivityRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Activities.objects.all()
    serializer_class = ActivitiesSerializer
    lookup_field = 'pk'

# ---------------------------------------------------------------------------- #
