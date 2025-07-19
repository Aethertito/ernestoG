from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['api_id', 'user_id', 'title', 'completed']
        widgets = {
            'api_id': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'ID del TODO en la API'
            }),
            'user_id': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'ID del usuario'
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Título del TODO'
            }),
            'completed': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            })
        }
        labels = {
            'api_id': 'ID de la API',
            'user_id': 'ID del Usuario',
            'title': 'Título',
            'completed': 'Completado'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Hacer que todos los campos sean requeridos excepto completed
        self.fields['api_id'].required = True
        self.fields['user_id'].required = True
        self.fields['title'].required = True
