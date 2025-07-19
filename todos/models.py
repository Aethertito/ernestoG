from django.db import models

class Todo(models.Model):
    # ID que viene de la API
    api_id = models.IntegerField(unique=True)
    # ID del usuario que viene de la API
    user_id = models.IntegerField()
    # Título del todo
    title = models.CharField(max_length=255)
    # Estado de completado
    completed = models.BooleanField(default=False)
    # Fecha de creación local
    created_at = models.DateTimeField(auto_now_add=True)
    # Fecha de última actualización
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['api_id']
        verbose_name = 'Todo'
        verbose_name_plural = 'Todos'

    def __str__(self):
        status = "✅" if self.completed else "❌"
        return f"{status} [{self.api_id}] {self.title[:50]}"

    @property
    def status_display(self):
        return "Resuelto" if self.completed else "Pendiente"
