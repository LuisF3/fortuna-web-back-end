from rest_framework import serializers

from company_profile.api.serializers import CompanySerializer
from student_profile.models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
