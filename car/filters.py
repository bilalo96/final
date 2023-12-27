import django_filters
from .models import Car


class CarFilters(django_filters.FilterSet):
    class Meta:
        model=Car
        fields=['name','description','category']