# Generated by Django 4.2.7 on 2023-12-04 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CVgenerator', '0005_cvtemplate_remove_userprofile_educations_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cvtemplate',
            name='additional_info',
            field=models.TextField(blank=True),
        ),
    ]
