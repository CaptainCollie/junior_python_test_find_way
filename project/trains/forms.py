from django import forms
from find_way.models import City
from .models import Train


class TrainForm(forms.ModelForm):
    name = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'form-control me-2',
        'placeholder': 'Train Number',
    }))
    travel_time = forms.IntegerField(label='', widget=forms.NumberInput(attrs={
        'class': 'form-control me-2',
        'placeholder': 'Travel Time',
    }))
    start_city = forms.ModelChoiceField(label='', queryset=City.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control me-2 js-basic-single',
    }))
    finish_city = forms.ModelChoiceField(label='', queryset=City.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control me-2 js-basic-single',
    }))

    class Meta:
        model = Train
        fields = '__all__'
