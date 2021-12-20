from rest_framework import viewsets
from rest_framework.response import Response
from .utils import get_data
from django.shortcuts import get_object_or_404
from .models import Car, Rating
from .serializers import CarSerializer, RatingSerializer, CarListSerializer, CarPopularSerializer
from rest_framework import status
from django.db.models import Count


class CarViewSet(viewsets.ViewSet):
    queryset = Car.objects.all()
    serializer = CarSerializer(queryset, many=True)

    def list(self, request):
        queryset = Car.objects.all()
        serializer = CarListSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        make = str(self.request.data.get('make'))
        model = str(self.request.data.get('model'))

        car_data = get_data(make=make)
        if car_data:
            for car in car_data:
                if car['Model_Name'] == model:
                    serializer = CarSerializer(data=request.data)
                    serializer.is_valid(raise_exception=True)
                    self.perform_create(serializer)
                    return Response(serializer.data, status=status.HTTP_201_CREATED)

            return Response(
                {'message': 'Model does not exist'},
                status=status.HTTP_400_BAD_REQUEST
            )
        return Response(
            {'message': 'Make does not exist'},
            status=status.HTTP_400_BAD_REQUEST
        )

    def perform_create(self, serializer):
        serializer.save()

    def destroy(self, request, id=None):
        queryset = Car.objects.all()
        car = get_object_or_404(queryset, id=id)
        instance = car
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()

class RatingViewSet(viewsets.ViewSet):
    queryset = Rating.objects.all()
    serializer = RatingSerializer(queryset, many=True)

    def create(self, request):
        car_id = request.data.get('car_id')
        rate = request.data.get('rate')
        if car_id and rate:
            serializer = RatingSerializer(data=self.request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                {'message': 'Missing data'},
                status=status.HTTP_400_BAD_REQUEST
            )

    def perform_create(self, serializer):
        serializer.save()

class PopularViewSet(viewsets.ViewSet):
    queryset = Car.objects.all()
    serializer_class = CarPopularSerializer

    def list(self, request):
        queryset = Car.objects.all().annotate(car_rating_count=Count('rating')).order_by(
            '-car_rating_count')
        serializer = CarPopularSerializer(queryset, many=True)
        return Response(serializer.data)
