from logging import raiseExceptions
from django.db.utils import IntegrityError
from django.test import TestCase
from ..models import Car, Rating

class CarTest(TestCase):
    def test_unique(self):
        car1 = Car.objects.create(make='Ford', model='Focus')
        with self.assertRaises(IntegrityError):
            car2 = Car.objects.create(make='Ford', model='Focus')

    def test_avg_rating(self):
        car1 = Car.objects.create(make='Ford', model='Focus')
        rating1 = Rating.objects.create(rate=3, car_id=car1)
        rating2 = Rating.objects.create(rate=5, car_id=car1)

        self.assertEqual(car1.avg_rating(), 4.0)

    def test_no_ratings(self):
        car1 = Car.objects.create(make='Ford', model='Focus')
        self.assertEqual(car1.avg_rating(), None)
        self.assertEqual(car1.rating_count(), 0)

    def test_rating_count(self):
        car1 = Car.objects.create(make='Ford', model='Focus')
        rating1 = Rating.objects.create(rate=3, car_id=car1)
        rating2 = Rating.objects.create(rate=5, car_id=car1)

        self.assertEqual(car1.rating_count(), 2)

    def test_str(self):
        car1 = Car.objects.create(make='Ford', model='Focus')
        self.assertIn(str(car1), '<Car: Focus made by Ford>')
