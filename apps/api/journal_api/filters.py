from django_filters import rest_framework as filters

from apps.journal.models import journal

class journalFilter(filters.FilterSet):
    class Meta:
        model = journal
        fields = ['portfolio', 'market', 'currency', 'created', 'updated']
