
from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        print(validated_data)
        password = validated_data.pop('password')
        print(password)
        print(validated_data)
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user
