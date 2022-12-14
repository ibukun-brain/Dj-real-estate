from time import time

from django.template.defaultfilters import slugify
from django.utils import timezone
from django.utils.timezone import now


def _upload_path(model, filetype, filename):
    """
    base function to generate upload path for media files to prevent duplicate
    """
    path = f"{filetype}/{model._meta.model_name}/{timezone.localdate()}"
    ext = filename.rsplit(".", 1)
    filename = slugify(f"{int(time())}-{ext[0]}")

    if len(ext) > 1:
        filename += "." + ext[-1]

    return f"{path}/{filename}"


def get_image_upload_path(model, filename):
    """generate upload path for images to prevent duplicate"""
    return _upload_path(model, "images", filename)