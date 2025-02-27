from django.urls import path
from .views import file_upload_main


urlpatterns = [
    path('', file_upload_main, name='file_management'),
]
