from rest_framework import serializers
from HireApp.models import Jobs, Applicants

class JobsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Jobs
        fields = ('JobId', 'Name')

class ApplicantsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Applicants
        fields = ('ApplicantId', 'Name', 'Status', 'Flag')