from django import forms
from .models import CarBook

class CarBookForm(forms.ModelForm):
    date_from=forms.DateField(widget=forms.DateInput(attrs={'id':'checkin_date'}))
    date_to=forms.DateField(widget=forms.DateInput(attrs={'id':'checkin_date'}))
    class Meta:
        model=CarBook
        fields=['date_from','date_to','guest','children']
