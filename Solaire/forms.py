
# ---------------------------------------------------------------------------- #

from django import forms
from .models import Activities

# ---------------------------------------------------------------------------- #

class ActivitiesForm(forms.ModelForm):
    
    class Meta:
        model = Activities
        fields = [ 'user', 'title', 'description', 'status' ]
        
        widgets = {
            'user': forms.Select(attrs={
                'class': 'form-control',
            }),

            'title': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Título de la actividad...'
            }),

            'description': forms.Textarea(attrs={
                'class': 'form-control', 'rows': 4,
                'placeholder': 'Descripción detallada de la actividad...'
            }),

            'status': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
        }

        labels = {
            'user': 'Usuario responsable',
            'title': 'Título',
            'description': 'Descripción',
            'status': 'Estado',
        }

# ---------------------------------------------------------------------------- #
