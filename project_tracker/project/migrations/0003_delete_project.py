# Generated by Django 4.0.1 on 2022-02-03 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_alter_project_status'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Project',
        ),
    ]
