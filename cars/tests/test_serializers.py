from rest_framework import serializers
from django.test import TestCase
from ..models import Rating, Car
from ..serializers import RatingSerializer, CarSerializer, CarListSerializer, CarPopularSerializer

class TestCarSerializer(TestCase):
    def setUp(self):
        self.car_attributes = {
            'make': 'Ford',
            'model': 'Fiesta'
        }

        self.car = Car.objects.create(**self.car_attributes)
        self.serializer = CarSerializer(instance=self.car)

    def test_contains_expected_fields(self):
        data = self.serializer.data

        self.assertEqual(set(data.keys()), set(['make', 'model']))

    def test_make_field_content(self):
        data = self.serializer.data

        self.assertEqual(data['make'], self.car_attributes['make'])

    def test_model_field_content(self):
        data = self.serializer.data

        self.assertEqual(data['model'], self.car_attributes['model'])

class TestCarListSerializer(TestCase):
    def setUp(self):
        self.car_attributes = {
            'make': 'Ford',
            'model': 'Fiesta'
        }

        self.car = Car.objects.create(**self.car_attributes)
        self.serializer = CarListSerializer(instance=self.car)

    def test_contains_expected_fields(self):
        data = self.serializer.data

        self.assertEqual(set(data.keys()), set(['make', 'model', 'avg_rating']))

    def test_make_field_content(self):
        data = self.serializer.data

        self.assertEqual(data['make'], self.car_attributes['make'])

    def test_model_field_content(self):
        data = self.serializer.data

        self.assertEqual(data['model'], self.car_attributes['model'])

    def test_avg_rating(self):
        data = self.serializer.data

        self.assertEqual(data['avg_rating'], None)

class TestCarPopularSerializer(TestCase):
    def setUp(self):
        self.car_attributes = {
            'make': 'Ford',
            'model': 'Fiesta'
        }

        self.car = Car.objects.create(**self.car_attributes)
        self.serializer = CarPopularSerializer(instance=self.car)

    def test_contains_expected_fields(self):
        data = self.serializer.data

        self.assertEqual(set(data.keys()), set(['make', 'model', 'rating_count']))

    def test_make_field_content(self):
        data = self.serializer.data

        self.assertEqual(data['make'], self.car_attributes['make'])

    def test_model_field_content(self):
        data = self.serializer.data

        self.assertEqual(data['model'], self.car_attributes['model'])

    def test_rating_count_field_content(self):
        data = self.serializer.data

        self.assertEqual(data['rating_count'], 0)
