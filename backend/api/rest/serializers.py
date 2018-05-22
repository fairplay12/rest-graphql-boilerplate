from django.contrib.auth.models import User
from rest_framework import serializers

from accounts.models import Employee, Employer
from jobs.models import Company, Business


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'first_name', 'last_name')


class EmployeeSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Employee
        fields = ('id', 'experience', 'company', 'user',)

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data.get('user').get('email'),
            username=validated_data.get('user').get('username'),
            first_name=validated_data.get('user').get('first_name'),
            last_name=validated_data.get('user').get('last_name')
        )
        instance = Employee.objects.create(
            experience=validated_data.get('experience'),
            user=user
        )

        return instance


class EmployerSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Employer
        fields = ('id', 'is_super_employer', 'user',)

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data.get('user').get('email'),
            username=validated_data.get('user').get('username'),
            first_name=validated_data.get('user').get('first_name'),
            last_name=validated_data.get('user').get('last_name')
        )
        instance = Employer.objects.create(
            is_super_employer=validated_data.get('is_super_employer'),
            user=user
        )

        return instance


class CompanySerializer(serializers.ModelSerializer):
    employees = serializers.SerializerMethodField()

    class Meta:
        model = Company
        fields = ('id', 'name', 'owner', 'business', 'employees')

    def get_employees(self, company):
        return EmployeeSerializer(company.employees, many=True).data


class BusinessSerializer(serializers.ModelSerializer):
    companies = serializers.SerializerMethodField()

    class Meta:
        model = Business
        fields = ('id', 'name', 'companies')

    def get_companies(self, business):
        return CompanySerializer(business.companies, many=True).data
