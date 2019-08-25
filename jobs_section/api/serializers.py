from rest_framework import serializers

from company_profile.api.serializers import CompanySerializer
from jobs_section.models import Job


class JobSerializer(serializers.ModelSerializer):
    company = CompanySerializer()

    class Meta:
        model = Job
        fields = '__all__'
