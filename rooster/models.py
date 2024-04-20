from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


# Create your models here.
class CrossOneself(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь', **NULLABLE)
    time = models.TimeField(verbose_name='время')
    action = models.CharField(max_length=600, verbose_name='действие')
    duration = models.DurationField(verbose_name='длительность')
    is_public = models.BooleanField(default=False, verbose_name="опубликовано")
    is_nice = models.BooleanField(default=False, verbose_name='это приятная привычка')
    period = models.SmallIntegerField(default=1, verbose_name='периодичность')
    place = models.CharField(max_length=600, verbose_name='место', **NULLABLE)
    chain_nice = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='вознаграждение-привычка', **NULLABLE)
    prise = models.CharField(max_length=300, verbose_name='вознаграждение', **NULLABLE)
    next_run = models.DateField(verbose_name='дата следующего выполнения', **NULLABLE)

    def __str__(self):
        if self.is_nice:
            return (f"'Приятная привычка {self.action} пользователя {self.user}")
        return (f"'Полезная привычка {self.action} пользователя {self.user}")
