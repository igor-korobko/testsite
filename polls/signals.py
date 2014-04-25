from django.core.files.storage import FileSystemStorage
from django.conf.global_settings import MEDIA_ROOT


def del_img(sender, **k):
    obj = k['instance']
    try:
        old_obj = sender.objects.get(pk=obj.pk)
    except(sender.DoesNotExist):
        pass
    else:
        if obj.img != old_obj.img:
            f = FileSystemStorage()
            f.delete(MEDIA_ROOT + sender.objects.get(pk=obj.pk).img.__str__())


def del_img_with_post(sender, **k):
    obj = k['instance']
    f = FileSystemStorage()
    f.delete(MEDIA_ROOT + obj.img.__str__())

