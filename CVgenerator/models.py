from django.db import models

class CVTemplate(models.Model):
    email = models.EmailField(unique=True)
    location = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    summary = models.TextField()
    wanted_job_title = models.CharField(max_length=255)
    skills = models.CharField(max_length=255)
    header_color = models.CharField(max_length=7)
    header_text_color = models.CharField(max_length=7)
    employments = models.JSONField(default=list)  # Store as JSON array
    educations = models.JSONField(default=list)  # Store as JSON array
    projects = models.JSONField(default=list)  # Store as JSON array
