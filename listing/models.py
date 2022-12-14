import uuid
import auto_prefetch
from django.db import models
from django.utils.text import slugify
from realestate.utils.models import TimeBasedModel
from realestate.utils.choices import ListingStatus
from realestate.utils.media import get_image_upload_path

# Create your models here.
class Listing(TimeBasedModel):
    realtor = auto_prefetch.ForeignKey(
        'home.Realtor',
        on_delete=models.SET_NULL,
        null=True
    )
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=6)
    description = models.TextField(blank=True)
    price = models.PositiveSmallIntegerField(default=0)
    bedrooms = models.PositiveIntegerField(default=0)
    bathrooms = models.PositiveSmallIntegerField(default=0)
    garage = models.PositiveSmallIntegerField(default=0)
    sqft = models.PositiveIntegerField(default=0)
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    status = models.CharField(
        choices=ListingStatus.choices, 
        max_length=50,
        default=ListingStatus.Pending)
    photo_main = models.ImageField(
        upload_to=get_image_upload_path,
        blank=True,
        verbose_name="Featured Listing Picture",
        null=True,
    )
    photo_1 = models.ImageField(
        upload_to=get_image_upload_path,
        blank=True,
        null=True,
    )
    photo_2 = models.ImageField(
        upload_to=get_image_upload_path,
        blank=True,
        null=True,
    )
    photo_3 = models.ImageField(
        upload_to=get_image_upload_path,
        blank=True,
        null=True,
    )
    photo_4 = models.ImageField(
        upload_to=get_image_upload_path,
        blank=True,
        null=True,
    )
    photo_5 = models.ImageField(
        upload_to=get_image_upload_path,
        blank=True,
        null=True,
    )
    photo_6 = models.ImageField(
        upload_to=get_image_upload_path,
        blank=True,
        null=True,
    )
   
    def save(self, *args, **kwargs):
        uuid_start = str(uuid.uuid1()).split("-", 1)[0]
        if not self.pk:
            self.slug = slugify(self.title) + "-" + uuid_start

        super().save()
    def __str__(self):
        return self.title