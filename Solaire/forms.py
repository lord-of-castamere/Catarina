
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
                'class': 'form-select',
                'data-placeholder': 'Usuario responsable'
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-char',
                'data-placeholder': 'Título/nombre para la actividad...'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-area', 'rows': 4,
                'placeholder': 'Descripción detallada de la actividad...'
            }),
            'status': forms.CheckboxInput(attrs={
                'class': 'form-boolean'
            })
        }

        labels = {
            'user': 'Responsable',
            'title': 'Título',
            'description': 'Descripción',
            'status': 'Estado',
        }

        help_texts = {
            'user': 'Seleccione al usuario responsable de esta actividad',
            'title': 'Ingrese un título para esta actividad.',
            'description': 'Ingrese una descripción detallada para esta actividad.',
            'status': 'Establezca el estado actual de la actividad (Completado/Pendiente).',
        }

# ---------------------------------------------------------------------------- #
