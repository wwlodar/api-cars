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
        fields = ['make', 'model', 'avg_rating']

class CarPopularSerializer(serializers.ModelSerializer):
    rating_count = serializers.SerializerMethodField()

    def get_rating_count(self, obj):
        return obj.rating_count()

    class Meta:
        model = Car
        fields = ['make', 'model', 'rating_count']
