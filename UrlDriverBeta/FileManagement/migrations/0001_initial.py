# Generated by Django 5.1.6 on 2025-02-27 18:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UrlManagement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_path', models.CharField(db_index=True, max_length=300)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'URL',
                'verbose_name_plural': 'URLs',
                'db_table': 'urls',
            },
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_attachment', models.FilePathField(blank=True, null=True, path='C:/TEMP', verbose_name='File')),
                ('file', models.TextField(blank=True, null=True, verbose_name='Criptografed File')),
                ('file_name', models.CharField(db_index=True, max_length=150, verbose_name='File Name')),
                ('version', models.PositiveIntegerField(default=0, verbose_name='File Version')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('file_path', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FileManagement.urlmanagement', verbose_name='File Path')),
            ],
            options={
                'verbose_name': 'File',
                'verbose_name_plural': 'Files',
                'db_table': 'file',
                'unique_together': {('file_path', 'version')},
            },
        ),
    ]
