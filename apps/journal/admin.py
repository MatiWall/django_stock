from django.contrib import admin

from .models import tradingStrategyChoices, currenciesChoices


admin.site.register(tradingStrategyChoices)
admin.site.register(currenciesChoices)