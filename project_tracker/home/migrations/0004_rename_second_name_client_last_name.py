# Generated by Django 4.0.1 on 2022-02-03 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_client'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='second_name',
            new_name='last_name',
        ),
    ]
