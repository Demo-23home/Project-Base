from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from core_apps.common.models import TimeStampedModel
from cloudinary.models import CloudinaryField


User = get_user_model()


def get_user_username(instance: "Profile") -> str:
    return instance.user.username


class Profile(TimeStampedModel):

    class Gender(models.TextChoices):
        MALE = ("male", _("Male"))
        FEMALE = ("female", _("Female"))

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    avatar = CloudinaryField("image", null=True, blank=True)
    gender = models.CharField(verbose_name=_("Gender"), choices=Gender.choices, default=Gender.MALE, max_length=6)
    bio = models.TextField(verbose_name=_("BIO"), blank=True, null=True)
    phone_number = PhoneNumberField(
        verbose_name=_("Phone Number"), default="+201017595972", max_length=13
    )
    country = CountryField(verbose_name=_("Country Field"), default="EGY")
    city_of_origin = models.CharField(verbose_name=_("City"), max_length=150, default="Cairo")
    report_count = models.IntegerField(verbose_name=_("Report Count"), default=0)
    reputation = models.IntegerField(verbose_name=_("Reputation"), default=100)
    slug = AutoSlugField(populate_from=get_user_username, unique=True)

    @property
    def is_banned(self) -> bool:
        return self.report_count >= 5

    def update_reputation(self) -> None:
        self.reputation = max(0, (100 - self.report_count * 20))

    def save(self, *args, **kwargs) -> None:
        self.update_reputation()
        super().save(*args, **kwargs)
