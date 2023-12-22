# filters.py
import django_filters
from .models import Restaurant

class RestaurantFilter(django_filters.FilterSet):
    min_average_rating = django_filters.NumberFilter(field_name='average_rating', lookup_expr='gt')

    class Meta:
        model = Restaurant
        fields = ['min_average_rating']
