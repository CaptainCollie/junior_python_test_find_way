from django.core.exceptions import ValidationError
from django.db import models

from find_way.models import City


class Train(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Train number")
    travel_time = models.PositiveIntegerField(verbose_name="Travel time")
    start_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='start_city_set', verbose_name='Start')
    finish_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='finish_city_set',
                                    verbose_name='Finish')

    def __str__(self):
        return f'Train #{self.name}, Start: {self.start_city}, Finish:{self.finish_city}'

    class Meta:
        verbose_name = 'Train'
        verbose_name_plural = 'Trains'
        ordering = ['travel_time']

    def clean(self):
        if self.start_city == self.finish_city:
            raise ValidationError('Start and Finish are same')
        qs = Train.objects.filter(
            start_city=self.start_city, finish_city=self.finish_city,
            travel_time=self.travel_time,
        ).exclude(pk=self.pk)
        if qs.exists():
            raise ValidationError("Travel time is incorrect")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
