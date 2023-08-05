from.models import Molel3
from django.forms import ModelForm, TextInput,widgets,Textarea


class Molel3Form(ModelForm):
    class Meta:
        model = Molel3
        fields = ['pole1','pole2']

        widgets = {
            "pole1":TextInput(attrs={
            'class':'form-control',
            'placeholder':'Название статьи'
        }),
         "pole2":Textarea(attrs={
            'class':'form-control',
            'placeholder':'Текст статьи'
            })
        }

