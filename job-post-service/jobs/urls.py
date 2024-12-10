from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JobViewSet

router = DefaultRouter()
router.register('', JobViewSet)  # Base URL for jobs: /api/jobs/

urlpatterns = [
    path('', include(router.urls)),
]
