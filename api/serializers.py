from rest_framework import serializers
from .models import Report, Actor, Company


class ReportSerializer(serializers.ModelSerializer):

    class Meta:
        model = Report
        fields = ('title', 'content', 'city', 'state', 'actor', 'company', 'user', 'created_date', 'updated_date')


class ActorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ('fName', 'lName', 'job_position')


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ('name', 'industry')
