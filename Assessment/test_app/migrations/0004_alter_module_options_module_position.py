# Generated by Django 4.0.6 on 2022-07-21 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0003_module'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='module',
            options={'ordering': ['position']},
        ),
        migrations.AddField(
            model_name='module',
            name='position',
            field=models.PositiveIntegerField(default=0),
        ),
    ]