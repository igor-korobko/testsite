from django.core.files.storage import FileSystemStorage
from django.conf.global_settings import MEDIA_ROOT


def del_img(sender, **k):
    obj = k['instance']
    try:
        old_obj = sender.objects.get(pk=obj.pk)
    except(sender.DoesNotExist):
        pass
    else:
        if old_obj.photo:
            if obj.photo != old_obj.photo:
                f = FileSystemStorage()
                f.delete(MEDIA_ROOT + sender.objects.get(pk=obj.pk).photo.__str__())


def del_img_with_post(sender, **k):
    obj = k['instance']
    f = FileSystemStorage()
    f.delete(MEDIA_ROOT + obj.photo.__str__())

