# Generated by Django 4.0.6 on 2022-07-21 07:08

from django.db import migrations, models
import test_app.validators
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256)),
                ('slug', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('image', models.ImageField(null=True, upload_to='', validators=[test_app.validators.validate_image_extension])),
                ('status', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]