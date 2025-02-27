from .models import File, UrlManagement
import traceback
from datetime import datetime

def upload_attachment(user, file, file_name, file_path):
    try:
        # kwargs = {
        #     'created_by': user,
        #     'file_attachment': file,
        #     'file_name': file_name,
        #     'created_at': datetime.now(),
        #     'file_path': file_path,
        # }

        new_file = File.objects.create(
            created_by=user,
            file_attachment=file,
            file_name=file_name,
            file_path=file_path
        )

        return new_file

    except Exception as ex:
        print(traceback.format_exc())
        return False
