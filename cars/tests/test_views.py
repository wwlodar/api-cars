from rest_framework.test import APIRequestFactory, APITestCase
from django.urls import reverse
import requests
import json
from ..models import Car, Rating
from rest_framework.test import APIClient
import mock
class TestGetCar(APITestCase):
    def test_get_no_cars(self):
        response = self.client.get(reverse("car-list"))
        self.assertEqual(200, response.status_code)

        response_data = json.loads(response.content)
        self.assertEqual([], response_data)

    def test_multiple_cars(self):
        car1 = Car.objects.create(make='Ford', model='Focus')
        rating1 = Rating.objects.create(rate=3, car_id=car1)
        rating2 = Rating.objects.create(rate=5, car_id=car1)
        car2 = Car.objects.create(make='Ford', model='Fiesta')

        response = self.client.get(reverse("car-list"))
        self.assertEqual(200, response.status_code)

        response_data = json.loads(response.content)
        self.assertEqual([{'avg_rating': 4.0, 'make': 'Ford', 'model': 'Focus'},
                          {'avg_rating': None, 'make': 'Ford', 'model': 'Fiesta'}], response_data)

class TestPostCar(APITestCase):

    @mock.patch('cars.views.get_data', return_value=[])
    def test_post_incorrect_make(self, mock_get_data):
        response = self.client.post(reverse("car-list"),
                                    {"make": "Fordwithmiastake", "model": "Focus"})
        self.assertEqual(400, response.status_code)

        response_data = json.loads(response.content)
        self.assertEqual({'message': 'Make does not exists'}, response_data)

    @mock.patch('cars.views.get_data', return_value=[
        {'Make_ID': 492, 'Make_Name': 'FIAT', 'Model_ID': 3490, 'Model_Name': 'Freemont'}])
    def test_post_incorrect_model(self, mock_get_data):
        response = self.client.post(reverse("car-list"),
                                    {"make": "Fiat", "model": "Panda"})
        self.assertEqual(400, response.status_code)

        response_data = json.loads(response.content)
        self.assertEqual({'message': 'Model does not exists'}, response_data)

    @mock.patch('cars.views.get_data', return_value=[
        {'Make_ID': 492, 'Make_Name': 'FIAT', 'Model_ID': 3490, 'Model_Name': 'Freemont'}])
    def test_post_correct(self, mock_get_data):
        response = self.client.post(reverse("car-list"),
                                    {"make": "Fiat", "model": "Freemont"})
        self.assertEqual(201, response.status_code)

        response_data = json.loads(response.content)
        self.assertEqual({'make': 'Fiat', 'model': 'Freemont'}, response_data)

    @mock.patch('cars.views.get_data', return_value=[
        {'Make_ID': 492, 'Make_Name': 'FIAT', 'Model_ID': 3490, 'Model_Name': 'Freemont'}])
    def test_existing_car(self, mock_get_data):
        car1 = Car.objects.create(make='Fiat', model='Freemont')
        response = self.client.post(reverse("car-list"),
                                    {"make": "Fiat", "model": "Freemont"})
        self.assertEqual(400, response.status_code)

        response_data = json.loads(response.content)
        self.assertEqual({'non_field_errors': ['The fields make, model must make a unique set.']}, response_data)

class TestDeleteCar(APITestCase):
    def test_delete_existing_car(self):
        pass

    def test_delete_nonexisting_car(self):
        pass

class TestGetPopular(APITestCase):
    def test_get_no_cars(self):
        response = self.client.get(reverse("popular-list"))
        self.assertEqual(200, response.status_code)

        response_data = json.loads(response.content)
        self.assertEqual([], response_data)

    def test_multiple_cars(self):
        car1 = Car.objects.create(make='Ford', model='Focus')
        rating1 = Rating.objects.create(rate=3, car_id=car1)
        rating2 = Rating.objects.create(rate=5, car_id=car1)
        car2 = Car.objects.create(make='Ford', model='Fiesta')
        rating3 = Rating.objects.create(rate=5, car_id=car2)

        response = self.client.get(reverse("popular-list"))
        self.assertEqual(200, response.status_code)

        response_data = json.loads(response.content)
        self.assertEqual([{'make': 'Ford', 'model': 'Focus', 'rating_count': 2},
                          {'make': 'Ford', 'model': 'Fiesta', 'rating_count': 1}], response_data)


class TestPostRating(APITestCase):
    def test_post_nonexistent_car(self):
        pass

    def test_incorrect_rate(self):
        pass

    def test_correct(self):
        pass
