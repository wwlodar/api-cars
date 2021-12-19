from django.urls import path
from rest_framework import routers
from django.views.generic.base import RedirectView
from .views import CarViewSet, RatingViewSet, PopularViewSet

router = routers.SimpleRouter()
router.register(r'cars', CarViewSet)
router.register(r'rate', RatingViewSet)
router.register(r'popular', PopularViewSet, basename='popular')

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='car-list'),
         name='cars_list'),
]
urlpatterns += router.urls
