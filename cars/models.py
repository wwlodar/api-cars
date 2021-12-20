from django.db import models
from django.db.models import Avg, Count
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, IntegerField
from django.core.validators import MaxValueValidator, MinValueValidator


class Car(models.Model):
    make = CharField(max_length=200)
    model = CharField(max_length=200)

    class Meta:
        unique_together = ['make', 'model']

    def avg_rating(self):
        return self.rating_set.aggregate(Avg('rate'))['rate__avg']

    def rates_number(self):
        return self.rating_set.aggregate(Count('rate'))['rate__count']

    def __str__(self):
        return f'{self.model} made by {self.make}'


class Rating(models.Model):
    rate = IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)
