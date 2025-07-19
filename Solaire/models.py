
# ---------------------------------------------------------------------------- #

from django.db import models
from django.contrib.auth.models import User

# ---------------------------------------------------------------------------- #

# Este modelito representa la 'pizarra' de actividades. 
class Activities(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
        related_name='UserActivities', verbose_name='Usuario responsable')

    title = models.CharField(max_length=64, verbose_name='Título')
    description = models.CharField(max_length=256, verbose_name='Descripción')

    status = models.BooleanField(default=False, verbose_name='Estado (Pendiente/Completada)')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Última actualización')

    class Meta:
        verbose_name = 'Actividad'
        verbose_name_plural = 'Actividades'
        ordering = [ 'status', '-created_at' ]

    def __str__(self):
        status = 'Completada' if self.status else 'Pendiente'
        return f'Actividad "{self.title}" del usuario "{self.user.username}" ({status})'

# ---------------------------------------------------------------------------- #
