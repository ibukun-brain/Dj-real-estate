import auto_prefetch
from django.conf import settings
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

from realestate.utils.models import TimeBasedModel
from realestate.utils.choices import Gender
from realestate.utils.media import get_image_upload_path



# Create your models here.
class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class CustomUser(TimeBasedModel, AbstractUser):
    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["email"]


    objects = UserManager()

    @property
    def is_realtor(self):
        return hasattrs(self, "realtor")
        
    class Meta(auto_prefetch.Model.Meta):
        ordering = ["first_name", "last_name"]
        verbose_name = "user"

    def __str__(self):
        return self.get_full_name() or self.email

class Realtor(TimeBasedModel):
    user = auto_prefetch.OneToOneField("home.CustomUser", on_delete=models.CASCADE)
    about = models.TextField(max_length=500, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    gender = models.CharField(
        max_length=15, choices=Gender.choices
    )
    profile_pic = models.ImageField(
        upload_to=get_image_upload_path,
        blank=True,
        verbose_name="Profile Picture",
        null=True,
    )
    is_mvp = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.user}"

    @property
    def image_url(self):
        """return image if it exists otherwise use a default"""
        if self.profile_pic:
            return self.profile_pic.url

        return f"{settings.STATIC_URL}img/realtors/default_avatar.png"


class Contact(TimeBasedModel):
    # user = auto_prefetch.ForeignKey(
    #     CustomUser,
    #     on_delete=models.SET_NULL,
    #     null=True,
    #     blank = True
    # )
    listing = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=15)
    message = models.TextField()


    def __str__(self):
        return self.listing