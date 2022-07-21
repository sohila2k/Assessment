# Generated by Django 4.0.6 on 2022-07-21 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='course',
            name='slug',
            field=models.CharField(max_length=256, unique=True),
        ),
    ]