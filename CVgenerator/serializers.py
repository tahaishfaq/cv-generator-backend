from rest_framework import serializers
from .models import CVTemplate

class CVTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CVTemplate
        fields = '__all__'
