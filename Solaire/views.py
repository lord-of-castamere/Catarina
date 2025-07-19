
# ---------------------------------------------------------------------------- #

import requests
from .forms import *
from django.views import generic
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import render, redirect

ACTIVITIES_URL = 'http://127.0.0.1:8000/api/v0/activities/'

# ---------------------------------------------------------------------------- #

class ListActivities(generic.View):
    template_name = 'Activities/List.html'

    def get(self, request):
        activities = []
        try:
            # Obtener todas las actividades de la API
            response = requests.get(ACTIVITIES_URL)
            response.raise_for_status()
            activities = response.json()
        except requests.exceptions.RequestException as e:
            messages.error(request, f'Ha ocurrido un error al conectar con la API')
            activities = []
        
        context = { 'activities': activities }
        return render(request, self.template_name, context)

# ---------------------------------------------------------------------------- #

class DetailActivities(generic.View):
    template_name = 'Activities/Detail.html'

    def get(self, request, pk):
        activity = None
        
        try:
            response = requests.get(f"{ACTIVITIES_URL}{pk}/")
            response.raise_for_status()
            activity = response.json()
        except requests.exceptions.RequestException as e:
            messages.error(request, f'Ha ocurrido un error al conectar con la API')
            return redirect('Solaire:ListActivities')
        except Exception as e:
            messages.error(request, f'Ha ocurrido al obtener la actividad.')
            return redirect('Solaire:ListActivities')
        
        context = { 'activity': activity }
        return render(request, self.template_name, context)

# ---------------------------------------------------------------------------- #

class CreateActivities(generic.View):
    template_name = 'Activities/Create.html'
    form_class = ActivitiesForm
    success_url = reverse_lazy('Solaire:ListActivities')

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        context = { 'form': form }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            try:
                response = requests.post(ACTIVITIES_URL, json=form.cleaned_data)
                response.raise_for_status()
                messages.success(request, 'Actividad creada exitosamente.')
                return redirect(self.success_url)
            except requests.exceptions.RequestException as e:
                messages.error(request, f'Ha ocurrido un error al crear la actividad')

            except Exception as e:
                messages.error(request, f'Ha ocurrido un error al crear la actividad')
        
        context = { 'form': form }
        return render(request, self.template_name, context)

# ---------------------------------------------------------------------------- #

class UpdateActivities(generic.View):
    template_name = 'Activities/Update.html'
    form_class = ActivitiesForm
    success_url = reverse_lazy('Solaire:ListActivities')

    def get(self, request, pk, *args, **kwargs):
        activity_data = None

        try:
            response = requests.get(f"{ACTIVITIES_URL}{pk}/")
            response.raise_for_status()
            activity_data = response.json()
            form = self.form_class(initial=activity_data)
        except requests.exceptions.RequestException as e:
            messages.error(request, f'Ha ocurrido un error al cargar los datos de la actividad.')
            return redirect(self.success_url)
        except Exception as e:
            messages.error(request, f'Ha ocurrido un error inesperado al cargar la actividad:')
            return redirect(self.success_url)
        
        context = { 'form': form, 'pk': pk }
        return render(request, self.template_name, context)

    def post(self, request, pk, *args, **kwargs):
        form = self.form_class(request.POST)
        
        if form.is_valid():
            try:
                response = requests.put(f"{ACTIVITIES_URL}{pk}/", json=form.cleaned_data)
                response.raise_for_status()
                messages.success(request, 'Actividad actualizada exitosamente.')
                return redirect(self.success_url)
            except requests.exceptions.RequestException as e:
                messages.error(request, f'Error al actualizar la actividad en la API.')
                
            except Exception as e:
                messages.error(request, f'Ha ocurrido un error inesperado al actualizar la actividad.')
        
        context = { 'form': form, 'pk': pk }
        return render(request, self.template_name, context)

# ---------------------------------------------------------------------------- #

class DeleteActivities(generic.View):
    template_name = 'Activities/Delete.html'
    success_url = reverse_lazy('Solaire:ListActivities')

    def get(self, request, pk, *args, **kwargs):
        activity = None

        try:
            response = requests.get(f"{ACTIVITIES_URL}{pk}/")
            response.raise_for_status()
            activity = response.json()
        except requests.exceptions.RequestException as e:
            messages.error(request, f'Error al cargar la actividad para eliminar.')
            return redirect(self.success_url)
        except Exception as e:
            messages.error(request, f'Error inesperado al obtener la actividad')
            return redirect(self.success_url)
        
        context = { 'activity': activity }
        return render(request, self.template_name, context)

    def post(self, request, pk, *args, **kwargs):
        try:
            response = requests.delete(f"{ACTIVITIES_URL}{pk}/")
            response.raise_for_status()
            messages.success(request, 'Actividad eliminada exitosamente.')
            return redirect(self.success_url)
        except requests.exceptions.RequestException as e:
            messages.error(request, f'Error al eliminar la actividad de la API.')
        except Exception as e:
            messages.error(request, f'Error inesperado al eliminar la actividad')
        
        return redirect('Solaire:ListActivities')

# ---------------------------------------------------------------------------- #
