# Generated by Django 4.0.1 on 2022-03-08 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0010_project_developer'),
    ]

    operations = [
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_id', models.IntegerField()),
                ('feed', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_id', models.IntegerField()),
                ('feed', models.TextField()),
            ],
        ),
    ]
