from django.db import models
from django.contrib.auth.models import User

NULLABLE = {'blank': True, 'null': True}


# Create your models here.
class CrossOneself(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    time = models.TimeField(verbose_name='время')
    action = models.CharField(max_length=600, verbose_name='действие')
    duration = models.DurationField(verbose_name='длительность')
    is_public = models.BooleanField(default=False, verbose_name="опубликовано")
    is_nice = models.BooleanField(default=False, verbose_name='это приятная привычка')
    period = models.SmallIntegerField(default=1, verbose_name='периодичность')
    place = models.CharField(max_length=600, verbose_name='место', **NULLABLE)
    chain_nice = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='вознаграждение-привычка', **NULLABLE)
    prise = models.CharField(max_length=300, verbose_name='вознаграждение', **NULLABLE)

    def __str__(self):
        if self.is_nice:
            return (f"'Приятная привычка {self.action} пользователя {self.user}:\n"
                    f"                   каждые {self.period} дней\n"
                    f"                   на протяжении {self.duration} секунд\n"
                    f"                   делать {self.action}.")
        else:
            return (f"'Полезная привычка {self.action} пользователя {self.user}:\n"
                    f"                   каждые {self.period} дней\n"
                    f"                   на протяжении {self.duration} секунд\n"
                    f"                   делать {self.action},\n"
                    f"                   за это можно {self.prise if self.prise
                                                        else self.chain_nice.action if self.chain_nice else 'ничего'}.")



