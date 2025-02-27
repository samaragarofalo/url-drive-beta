import traceback
from django.http import HttpResponse
from django.shortcuts import render

from .models import UrlManagement


def file_upload_main(request):
    dic = dict()

    dic['url'] = UrlManagement.objects.filter(created_by__email=request.user.email).values_list('id', 'url_path')

    return render(request,'FileManagement/file-management.html', dic)


def file_upload(request):
    try:
        ...
    except Exception as e:
        print(e)
        print(traceback.format_exc())

    return HttpResponse()


def file_download(request):
    try:
        ...
    except Exception as e:
        print(e)
        print(traceback.format_exc())

    return HttpResponse()
