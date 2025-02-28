from .models import File, UrlManagement
import traceback


def upload_attachment(user, file, file_name, file_path):
    try:

        new_file = File.objects.create(
            created_by=user,
            file_attachment=file.read(),
            file_name=file_name,
            file_path=file_path,
        )

        return new_file

    except Exception as ex:
        print(traceback.format_exc())
        return False
