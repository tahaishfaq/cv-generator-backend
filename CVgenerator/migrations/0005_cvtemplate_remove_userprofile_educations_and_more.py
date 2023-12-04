# Generated by Django 4.2.7 on 2023-11-28 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CVgenerator', '0004_userprofile_delete_cvtemplate_delete_resumesettings'),
    ]

    operations = [
        migrations.CreateModel(
            name='CVTemplate',
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
                ('employments', models.JSONField(default=list)),
                ('educations', models.JSONField(default=list)),
                ('projects', models.JSONField(default=list)),
            ],
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='educations',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='employments',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='projects',
        ),
        migrations.DeleteModel(
            name='Education',
        ),
        migrations.DeleteModel(
            name='Employment',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
