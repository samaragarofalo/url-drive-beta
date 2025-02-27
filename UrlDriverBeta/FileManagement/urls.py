from django.urls import path, re_path
from .views import file_upload_main, file_upload, file_download


urlpatterns = [
    path('', file_upload_main, name='file_management'),
    path('post/', file_upload, name='file_upload'),
    re_path(r'^(?P<file_path>.+)$', file_download, name='file_download'),
]
