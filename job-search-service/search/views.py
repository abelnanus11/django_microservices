from rest_framework.generics import ListAPIView
from .models import Job
from .serializers import JobSerializer

class JobSearchView(ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        title = self.request.query_params.get('title')
        company = self.request.query_params.get('company')
        if title:
            queryset = queryset.filter(title__icontains=title)
        if company:
            queryset = queryset.filter(company__icontains=company)
        return queryset
