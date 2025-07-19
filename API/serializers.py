
# ---------------------------------------------------------------------------- #

from Solaire.models import Activities
from rest_framework import serializers
from django.contrib.auth.models import User

# ---------------------------------------------------------------------------- #

class ActivitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activities
        fields = '__all__'

# ---------------------------------------------------------------------------- #

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ 'id', 'username', 'email', 'first_name', 'last_name' ]

# ---------------------------------------------------------------------------- #

