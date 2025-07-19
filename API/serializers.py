
# ---------------------------------------------------------------------------- #

from Solaire.models import Activities
from rest_framework import serializers
from django.contrib.auth.models import User

# ---------------------------------------------------------------------------- #

class ActivitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activities
        fields = '__all__'

class ActivitiesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activities
        fields = '__all__'
        depth = 1

# ---------------------------------------------------------------------------- #

