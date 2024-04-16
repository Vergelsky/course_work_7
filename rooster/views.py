from django.contrib.auth.models import User
from rest_framework import viewsets

from rooster.models import CrossOneself
from rooster.serializers import CrossOneselfSerializer, UserSerializer


# Create your views here.
class CrossOneselfViewSet(viewsets.ModelViewSet):
    serializer_class = CrossOneselfSerializer
    queryset = CrossOneself.objects.all()

    # def perform_create(self, serializer):
    #     user = self.request.user
    #     serializer.save(user=user)


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
