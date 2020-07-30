from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault

from apps.journal.models import portfolio, journal

class portfolioSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = portfolio
        fields = ['id', 'name', 'notes', 'selected']






class journalSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = journal
        fields = ['id', 'portfolio', 'market', 'ticker', 'name', 'currency', 'strategy', 'found_via', 'notes']

    def get_fields(self):
        # get the original field names to field instances mapping
        fields = super(journalSerializer, self).get_fields()
    
        # modify the queryset
        fields['portfolio'].queryset = portfolio.objects.filter(user=self.context['request'].user)
        # return the modified fields mapping
        return fields


  