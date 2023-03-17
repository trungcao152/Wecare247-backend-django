from rest_framework import routers
from django.urls import path, include
from .views import CaregiverViewSet, ShiftViewSet, CustomerViewSet

router = routers.DefaultRouter()
router.register(r'caregivers', CaregiverViewSet, basename='caregivers')
router.register(r'shifts', ShiftViewSet, basename='shifts')
router.register(r'customers', CustomerViewSet, basename='customers')

urlpatterns = [
    path('', include(router.urls)),
]
