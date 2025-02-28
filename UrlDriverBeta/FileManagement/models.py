import os.path

from django.db import models
from django.contrib.auth.models import User


def define_upload_path(instance, file_name):
    return os.path.join(instance.file_path.url_path, f'v{instance.version}_{file_name}')


class UrlManagement(models.Model):
    url_path = models.CharField(max_length=300, db_index=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.url_path} - {self.created_by.email}'


    class Meta:
        db_table = "urls"
        verbose_name = "URL"
        verbose_name_plural = "URLs"


class File(models.Model):
    file_attachment = models.BinaryField(blank=True, null=True, verbose_name='File')
    file_name = models.CharField(max_length=150, db_index=True, verbose_name='File Name')
    file_path = models.ForeignKey(UrlManagement, on_delete=models.CASCADE, verbose_name='File Path')
    version = models.PositiveIntegerField(default=0, verbose_name='File Version')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.file_name} - (v{self.version}) - {self.file_path}'


    class Meta:
        db_table = "file"
        verbose_name = "File"
        verbose_name_plural = "Files"
