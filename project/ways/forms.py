from django import forms
from find_way.models import City
from .models import Way
from trains.models import Train


class WayForm(forms.ModelForm):
    start_city = forms.ModelChoiceField(label='Start', queryset=City.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control js-basic-single',
    }))
    finish_city = forms.ModelChoiceField(label='Finish', queryset=City.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control js-basic-single',
    }))
    btw = forms.ModelMultipleChoiceField(label='Between', queryset=City.objects.all(), required=False,
                                         widget=forms.SelectMultiple(
                                             attrs={
                                                 'class': 'form-control js-basic-multiple',
                                             }))

    # travel_time = forms.IntegerField(label='', widget=forms.NumberInput(attrs={
    #     'class': 'form-control',
    #     'placeholder': 'Travel Time',
    # }))

    class Meta:
        model = Way
        fields = ('start_city', 'finish_city')
