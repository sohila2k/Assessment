# Generated by Django 4.0.6 on 2022-07-21 10:25

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0002_course_is_deleted_alter_course_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('course_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='course_create', to='test_app.course')),
                ('parent_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='test_app.module')),
            ],
        ),
    ]