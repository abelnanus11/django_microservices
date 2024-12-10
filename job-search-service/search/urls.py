from django.urls import path
from .views import JobSearchView

urlpatterns = [
    path('', JobSearchView.as_view(), name='job-search'),
]
