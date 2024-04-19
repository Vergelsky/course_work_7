from django.contrib.auth.models import User
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from rooster.models import CrossOneself
from rooster.pagination import CrossOneselfPagination
from rooster.permissions import IsUserCreater
from rooster.serializers import CrossOneselfSerializer, UserSerializer


class CrossOneselfViewSet(viewsets.ModelViewSet):
    serializer_class = CrossOneselfSerializer
    pagination_class = CrossOneselfPagination

    def get_queryset(self):
        user = self.request.user
        return CrossOneself.objects.filter(user=user)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class PublicCrossOneselfListView(generics.ListAPIView):
    serializer_class = CrossOneselfSerializer
    pagination_class = CrossOneselfPagination

    def get_queryset(self):
        return CrossOneself.objects.filter(is_public=True)


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
