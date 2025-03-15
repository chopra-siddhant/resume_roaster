from rest_framework import serializers
from .models import Resume, HRSimulator, LinkedInFlex

class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = '__all__'

class HRSimulatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = HRSimulator
        fields = '__all__'

class LinkedInFlexSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinkedInFlex
        fields = '__all__'
