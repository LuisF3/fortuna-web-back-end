from rest_framework import viewsets, filters

from student_profile.api.serializers import StudentSerializer
from student_profile.models import Student


class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
