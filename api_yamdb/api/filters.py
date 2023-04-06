import django_filters

from reviews.models import Title


class TitleFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(lookup_expr='slug')
    genre = django_filters.CharFilter(lookup_expr='slug')
    name = django_filters.CharFilter(
        lookup_expr='icontains')

    class Meta:
        model = Title
        fields = '__all__'
