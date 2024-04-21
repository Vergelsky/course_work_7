from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from rooster.models import CrossOneself
from users.models import User


class RoosterTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email='testuser@mail.com')
        self.client.force_authenticate(user=self.user)
        self.cross_oneself = CrossOneself.objects.create(
            user=self.user,
            time="14:12:00",
            action="Действие привычки теста",
            duration="00:02:00"
        )
        print(self.cross_oneself, '\n', self.user)
        self.data = {
            "time": "14:12:00",
            "action": "Действие привычки теста",
            "duration": "00:02:00"
        }

    def test_create_cross_oneself(self):
        """Тестируем создание привычки"""

        self.client.force_authenticate(user=self.user)
        response = self.client.post(reverse('rooster:crossoneself-list'), data=self.data)

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_read_cross_oneself(self):
        """ Тестируем чтение списка привычек """

        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('rooster:crossoneself-list'), data=self.data)
        print(response.data)
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_update_cross_oneself(self):
        """ Тестируем обновление привычки """

        self.client.force_authenticate(user=self.user)
        response = self.client.patch(reverse('rooster:crossoneself-detail', args=[self.cross_oneself.pk]),
                                     data={'action': 'Новое действие теста'})
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_delete_cross_oneself(self):
        """ Тестируем удаление привычки """

        self.client.force_authenticate(user=self.user)
        response = self.client.delete(reverse('rooster:crossoneself-detail', args=[self.cross_oneself.pk]))
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
