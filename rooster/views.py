from datetime import timedelta, datetime

from rest_framework import viewsets, generics

from rooster.models import CrossOneself
from rooster.pagination import CrossOneselfPagination
from rooster.serializers import CrossOneselfSerializer


class CrossOneselfViewSet(viewsets.ModelViewSet):
    serializer_class = CrossOneselfSerializer
    pagination_class = CrossOneselfPagination

    def get_queryset(self):
        user = self.request.user
        return CrossOneself.objects.filter(user=user)

    def perform_create(self, serializer):
        instance = serializer.save()
        # data_to_task = {'time': instance.time.strftime('%H:%M:%S'), 'action': instance.action,
        #                 'user_id': instance.user.first_name}
        # create_iteration_task(f'rooster.tasks.periodic_peck)',
        #                       days=instance.period,
        #                       name=f'Отправка напоминания для {instance.action}',
        #                       **data_to_task)
        next_run = datetime.now().date() + timedelta(days=instance.period)
        return serializer.save(user=self.request.user, next_run=next_run)


class PublicCrossOneselfListView(generics.ListAPIView):
    serializer_class = CrossOneselfSerializer
    pagination_class = CrossOneselfPagination

    def get_queryset(self):
        return CrossOneself.objects.filter(is_public=True)
