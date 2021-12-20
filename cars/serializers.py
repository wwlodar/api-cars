from rest_framework import serializers
from .models import Car, Rating

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['make', 'model']

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['car_id', 'rate']

class CarListSerializer(serializers.ModelSerializer):
    avg_rating = serializers.SerializerMethodField()

    def get_avg_rating(self, obj):
        return obj.avg_rating()

    class Meta:
        model = Car
        fields = ['id', 'make', 'model', 'avg_rating']

class CarPopularSerializer(serializers.ModelSerializer):
    rates_number = serializers.SerializerMethodField()

    def get_rates_number(self, obj):
        return obj.rates_number()

    class Meta:
        model = Car
        fields = ['id', 'make', 'model', 'rates_number']
