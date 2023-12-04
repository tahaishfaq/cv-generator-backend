from rest_framework import generics
from .models import CVTemplate
from .serializers import CVTemplateSerializer

class CVTemplateListCreateView(generics.ListCreateAPIView):
    queryset = CVTemplate.objects.all()
    serializer_class = CVTemplateSerializer

class CVTemplateRetrieveView(generics.RetrieveAPIView):
    queryset = CVTemplate.objects.all()
    serializer_class = CVTemplateSerializer


class CVTemplateListView(generics.ListAPIView):
    queryset = CVTemplate.objects.all()
    serializer_class = CVTemplateSerializer