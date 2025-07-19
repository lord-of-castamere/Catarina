
# ---------------------------------------------------------------------------- #

from .serializers import *
from rest_framework import generics
from Solaire.models import Activities
from django.contrib.auth.models import User

# ---------------------------------------------------------------------------- #

class ActivityActiveListView(generics.ListAPIView):
    queryset = Activities.objects.filter(status=True)
    serializer_class = ActivitiesSerializer

class ActivityInactiveListView(generics.ListAPIView):
    queryset = Activities.objects.filter(status=False)
    serializer_class = ActivitiesSerializer

# ---------------------------------------------------------------------------- #

class ActivityListCreateView(generics.ListCreateAPIView):
    queryset = Activities.objects.all()
    serializer_class = ActivitiesSerializer

# ---------------------------------------------------------------------------- #

class ActivityRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Activities.objects.all()
    serializer_class = ActivitiesSerializer
    lookup_field = 'pk'

# ---------------------------------------------------------------------------- #

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# ---------------------------------------------------------------------------- #
