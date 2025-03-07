import io
import os.path
import traceback
import mimetypes

from django.db.models import QuerySet
from django.http import HttpResponse, JsonResponse, Http404, FileResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from .models import UrlManagement, File
from .utils import upload_attachment


@login_required(login_url="/login/")
def file_upload_main(request):
    dic = dict()

    dic['urls'] = UrlManagement.objects.filter(created_by__email=request.user.email).values_list('id', 'url_path')

    return render(request,'FileManagement/file-management.html', dic)


@login_required(login_url="/login/")
@csrf_exempt
def file_upload(request):
    try:
        uploaded_file = request.FILES.get('file')
        latest_version = None

        if not uploaded_file:
            return JsonResponse({"error": "No file uploaded."}, status=400)

        response = dict(request.POST)
        file_response = {k: v[0] for k, v in response.items()}

        type_of_url, create_or_get = ('create', 'new_url') if file_response['new_url'] else ('filter', 'url')

        file_path = eval(f"UrlManagement.objects.{type_of_url}(url_path=file_response['{create_or_get}'], "
                         f"created_by=request.user)")

        if create_or_get == 'url':
            latest_version = File.objects.filter(file_path=file_path[0]).last()

        new_file = upload_attachment(
            request.user,
            uploaded_file,
            uploaded_file.name,
            file_path[0] if isinstance(file_path, QuerySet) else file_path,
        )

        new_file.version = latest_version.version + 1 if latest_version else 0
        new_file.save()

    except Exception as e:
        print(e)
        print(traceback.format_exc())
        return JsonResponse({'message': 'Error while uploading file.'}, status=400)

    return JsonResponse({
        'message': "Your file was uploaded successfully!",
        'file_id': new_file.id,
    })


@login_required(login_url="/login/")
def file_download(request, file_path):
    try:
        revision = {k: v[0] for k, v in request.GET.items()}

        file_name = file_path.rsplit('/', 1)[-1]
        url = file_path.rsplit('/', 1)[0]

        url_path = get_object_or_404(UrlManagement, url_path=url)

        if 'revision' in revision:
            file = get_object_or_404(File, file_path=url_path, version=int(revision['revision']),
                                     created_by=request.user)
        else:
            file = File.objects.filter(file_path=url_path, created_by=request.user).order_by('-version').first()

        if not file or not file.file_attachment:
            raise Http404("File not found")

        guessed_mime_type, _ = mimetypes.guess_file_type(file.file_name)
        if not guessed_mime_type:
            guessed_mime_type = "application/octet-stream"

        response = FileResponse(io.BytesIO(file.file_attachment), as_attachment=True)
        response['Content-Disposition'] = f'attachment; filename="{file.file_name}"'
        response['Content-Type'] = guessed_mime_type

        return response

    except Exception as e:
        print(e)
        print(traceback.format_exc())
        raise Http404("Request could not be processed.")

    return HttpResponse()
