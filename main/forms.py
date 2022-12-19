from .models import Teachers
from django.forms import ModelForm, TextInput, DateInput

class TeachersForm(ModelForm):
    class Meta:
        model = Teachers
        fields = ['subject', 'first_name', 'second_name', 'date']

        widgets={
            'subject': TextInput(attrs={
                'class':'form-control',
                'placeholder':'Предмет учителя'
            }),
            'first_name': TextInput(attrs={
                'class':'form-control',
                'placeholder':'Имя учителя'
            }),
            'date': DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата запроса'
            }),
            'second_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия учителя'
            })
        }

