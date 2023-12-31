# Generated by Django 4.2.7 on 2023-11-28 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CVgenerator', '0003_education_employment_project_resumesettings_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('location', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=15)),
                ('summary', models.TextField()),
                ('wanted_job_title', models.CharField(max_length=255)),
                ('skills', models.CharField(max_length=255)),
                ('header_color', models.CharField(max_length=7)),
                ('header_text_color', models.CharField(max_length=7)),
                ('educations', models.ManyToManyField(to='CVgenerator.education')),
                ('employments', models.ManyToManyField(to='CVgenerator.employment')),
                ('projects', models.ManyToManyField(to='CVgenerator.project')),
            ],
        ),
        migrations.DeleteModel(
            name='CVTemplate',
        ),
        migrations.DeleteModel(
            name='ResumeSettings',
        ),
    ]
