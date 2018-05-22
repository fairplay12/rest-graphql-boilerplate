from api.rest.serializers import (UserSerializer, EmployeeSerializer,
                                  EmployerSerializer, CompanySerializer,
                                  BusinessSerializer)
from django.contrib.auth.models import User
from rest_framework import viewsets

from accounts.models import Employee, Employer
from jobs.models import Company, Business


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployerViewSet(viewsets.ModelViewSet):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class BusinessViewSet(viewsets.ModelViewSet):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer
