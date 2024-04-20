from rest_framework import serializers

from rooster.models import CrossOneself
from rooster.validators import NiceOrHelpfulValidator, ChainIsNiceValidator, \
    NiceWithoutPriseOrNice, DurationValidator, PeriodValidator


class CrossOneselfSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrossOneself
        fields = '__all__'
        validators = [NiceOrHelpfulValidator(fields=['is_nice', 'prise']),
                      DurationValidator(fields=['duration']),
                      PeriodValidator(fields=['period']),
                      NiceWithoutPriseOrNice(fields=['chain_nice', 'prise']),
                      ChainIsNiceValidator(fields=['chain_nice'])
                      ]
