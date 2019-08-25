from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response

from company_profile.api.serializers import CompanySerializer
from company_profile.models import Company
from jobs_section.api.serializers import JobSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    @action(detail=False, methods=['post'])
    def jobs(self, request):
        to_remove = list()
        for item in request.data:
            if item is None or item is '':
                to_remove.append(item)
        for item in to_remove:
            del request.data[item]

        cnpj = request.data['cnpj']
        jobs = Company.objects.get(cnpj=cnpj).job_set
        return Response(JobSerializer(jobs, many=True).data, status=status.HTTP_200_OK)
