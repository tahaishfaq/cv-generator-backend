from django.urls import path
from .views import CVTemplateListCreateView, CVTemplateRetrieveView, CVTemplateListView

urlpatterns = [
    path('cv-templates/', CVTemplateListCreateView.as_view(), name='cv-template-list-create'),
    path('cv-templates/<int:pk>/', CVTemplateRetrieveView.as_view(), name='cv-template-retrieve'),
    path('cv-templates/all/', CVTemplateListView.as_view(), name='cv-template-list'),
]
