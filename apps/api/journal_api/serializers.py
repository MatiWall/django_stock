from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault

from apps.journal.models import portfolio, Journal, JournalAction, JournalTargets

class portfolioSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = portfolio
        fields = ['id', 'name', 'notes', 'selected']






class journalSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Journal
        fields = ['id', 'portfolio', 'market', 'ticker', 'name', 'currency', 'strategy', 'found_via', 'notes', 'created']

    def get_fields(self):
        # get the original field names to field instances mapping
        fields = super(journalSerializer, self).get_fields()
    
        # modify the queryset
        fields['portfolio'].queryset = portfolio.objects.filter(user=self.context['request'].user)
        # return the modified fields mapping
        return fields


  

class journalActionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = JournalAction
        fields = ['id', 'action', 'action_reason', 'price', 'commision', 'fees', 'created', 'updated']

  
class journalTargetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = JournalTargets
        fields = ['id', 'shares', 'target_price', 'stop_loss', 'created', 'updated']