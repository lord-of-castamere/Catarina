
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
            response = requests.get(f"{ACTIVITIES_URL}list/")

            response.raise_for_status()
            activities = response.json()
        except requests.exceptions.RequestException as e:
            messages.error(request, f'Ha ocurrido un error al conectar con la API')
            activities = []
        
        context = { 'activities': activities }
        return render(request, self.template_name, context)


class ListCompletedActivities(generic.View):
    template_name = 'Activities/Completed.html'

    def get(self, request):
        activities = []
        try:
            # Obtener todas las actividades de la API
            response = requests.get(f"{ACTIVITIES_URL}completed/")

            response.raise_for_status()
            activities = response.json()
        except requests.exceptions.RequestException as e:
            messages.error(request, f'Ha ocurrido un error al conectar con la API')
            activities = []
        
        context = { 'activities': activities }
        return render(request, self.template_name, context)


class ListPendingActivities(generic.View):
    template_name = 'Activities/Pending.html'

    def get(self, request):
        activities = []
        try:
            # Obtener todas las actividades de la API
            response = requests.get(f"{ACTIVITIES_URL}pending/")

            response.raise_for_status()
            activities = response.json()
        except requests.exceptions.RequestException as e:
            messages.error(request, f'Ha ocurrido un error al conectar con la API')
            activities = []
        
        context = { 'activities': activities }
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
            cleaned_data = form.cleaned_data
            user_id = cleaned_data['user'].id

            data_to_send = {
                'user': user_id,
                'title': cleaned_data['title'],
                'description': cleaned_data['description'],
                'status': cleaned_data['status'],
            }

            try:
                response = requests.post(f"{ACTIVITIES_URL}create/", json=data_to_send)
                response.raise_for_status()
                messages.success(request, 'Actividad creada exitosamente.')
                return redirect(self.success_url)
            except requests.exceptions.RequestException as e:
                messages.error(request, f'Ha ocurrido un error al crear la actividad: {e}')

                if response is not None and hasattr(response, 'json'):
                    try:
                        error_details = response.json()
                        print(f"Detalles del error de la API: {error_details}")
                    except ValueError:
                        print(f"Respuesta de error de la API no es JSON: {response.text}")
            except Exception as e:
                messages.error(request, f'Ha ocurrido un error inesperado al crear la actividad: {e}')
                print(f"Error inesperado: {e}")
        
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
            
            if 'user' in activity_data and isinstance(activity_data['user'], dict):
                initial_user_id = activity_data['user']['id']
            elif 'user' in activity_data:
                initial_user_id = activity_data['user']
            else:
                initial_user_id = None

            initial_form_data = {
                'user': initial_user_id,
                'title': activity_data.get('title'),
                'description': activity_data.get('description'),
                'status': activity_data.get('status'),
            }

            form = self.form_class(initial=initial_form_data)

        except requests.exceptions.RequestException as e:
            messages.error(request, f'Ha ocurrido un error al cargar los datos de la actividad: {e}')
            print(f"Error en GET de API: {e}")
            if response is not None and hasattr(response, 'text'):
                print(f"Respuesta de API (GET): {response.text}")
            return redirect(self.success_url)
        except Exception as e:
            messages.error(request, f'Ha ocurrido un error inesperado al cargar la actividad: {e}')
            print(f"Error inesperado en GET: {e}")
            return redirect(self.success_url)
        
        context = { 'form': form, 'pk': pk }
        return render(request, self.template_name, context)

    def post(self, request, pk, *args, **kwargs):
        form = self.form_class(request.POST)
        
        if form.is_valid():
            cleaned_data = form.cleaned_data
            user_id = cleaned_data['user'].id 
            
            data_to_send = {
                'user': user_id,
                'title': cleaned_data['title'],
                'description': cleaned_data['description'],
                'status': cleaned_data['status'],
            }

            try:
                response = requests.put(f"{ACTIVITIES_URL}{pk}/", json=data_to_send)
                response.raise_for_status()
                messages.success(request, 'Actividad actualizada exitosamente.')
                return redirect(self.success_url)
            except requests.exceptions.RequestException as e:
                error_message = f'Error al actualizar la actividad en la API: {e}'
                if response is not None:
                    try:
                        error_details = response.json()
                        error_message += f" Detalles: {error_details}"
                    except ValueError:
                        error_message += f" Respuesta no JSON: {response.text}"
                messages.error(request, error_message)
                print(error_message)
            except Exception as e:
                messages.error(request, f'Ha ocurrido un error inesperado al actualizar la actividad: {e}')
                print(f"Error inesperado en PUT: {e}")
        
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
        print(context)
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
