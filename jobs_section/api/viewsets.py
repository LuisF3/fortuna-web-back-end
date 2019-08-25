from rest_framework import viewsets, filters, status
from rest_framework.response import Response

from company_profile.models import Company
from jobs_section.api.serializers import JobSerializer
from jobs_section.models import Job


class JobViewSet(viewsets.ModelViewSet):
    serializer_class = JobSerializer
    queryset = Job.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description', 'company__name', 'local', 'work_load', 'ingress_year', 'graduate_year', 'course']

    def create(self, request, *args, **kwargs):
        data = request.data
        print(data)
        company = data['company']
        del data['company']
        company = Company.objects.get(id=company)
        job = Job.objects.create(company=company, **data)
        return Response(JobSerializer(job).data, status=status.HTTP_204_NO_CONTENT)
