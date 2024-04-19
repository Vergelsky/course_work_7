from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

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


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user
