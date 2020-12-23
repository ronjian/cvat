# Generated by Django 3.1.1 on 2020-12-18 17:51

import cvat.apps.engine.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('engine', '0035_data_storage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='storage',
            field=models.CharField(choices=[('cloud_storage', 'CLOUD_STORAGE'), ('local', 'LOCAL'), ('share', 'SHARE')], default=cvat.apps.engine.models.StorageChoice['LOCAL'], max_length=15),
        ),
        migrations.CreateModel(
            name='CloudStorage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provider_type', models.CharField(choices=[('AWS_S3_BUCKET', 'AWS_S3'), ('AZURE_CONTAINER', 'AZURE_CONTAINER'), ('GOOGLE_DRIVE', 'GOOGLE_DRIVE')], max_length=20)),
                ('resource_name', models.CharField(max_length=50)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('credentials', models.CharField(max_length=100, unique=True)),
                ('credentials_type', models.CharField(choices=[('TOKEN', 'TOKEN'), ('KEY_TOKEN_PAIR', 'KEY_TOKEN_PAIR'), ('KEY_SECRET_KEY_PAIR', 'KEY_SECRET_KEY_PAIR')], max_length=20)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cloud_storages', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'default_permissions': (),
                'unique_together': {('provider_type', 'resource_name', 'credentials')},
            },
        ),
        migrations.AddField(
            model_name='data',
            name='cloud_storage',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='data', to='engine.cloudstorage'),
        ),
    ]