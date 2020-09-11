import base64
import zipfile
from django.core.files.base import ContentFile
from django.conf import settings
import os       
from .simple_ms1 import simple_ms1_processor


def handle_uploaded_file(f, view_name):
    # print(type(f), '*'*10)
    myfiles = []
    with zipfile.ZipFile(f) as z:
        z.extractall('documents/' + view_name)
    print('finished unzip!')
    simple_ms1_processor()
    return []
            # for f in z.namelist():

            #     suffix = f.split(".")[-1]

            #     if suffix in ['txt', 'mzML', 'csv', 'R']:
            #     # myfiles.append({f: base64.b64encode(z.read(f)),})
            #         z.extract(f, 'documents')
            #         myfiles.append(f)
    # r = process(myfiles)
       


# def process(myfiles):
#     newfiles = []
#     for f in myfiles:
#         os.rename(settings.MEDIA_ROOT +'/' + f, settings.MEDIA_ROOT +'/new_'+f.split("/")[-1])
#         newfiles.append('new_'+f.split("/")[-1])
#     return newfiles