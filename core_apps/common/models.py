from django.db import IntegrityError, models
import uuid
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


User = get_user_model()


class TimeStampedModel(models.Model):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ["-created_at", "-updated_at"]


class ContentView(TimeStampedModel):
    # stores a recreance to content-type instance, corresponding to the model of the object begin viewed
    content_type = models.ForeignKey(
        ContentType, verbose_name=_("Content Type"), on_delete=models.CASCADE
    )
    object_id = models.PositiveIntegerField(_("Object ID"))
    # Django model instance that is being viewed
    content_object = GenericForeignKey("content_type", "object_id")
    user = models.ForeignKey(
        User,
        verbose_name=_("User"),
        on_delete=models.CASCADE,
        related_name="content_views",
        null=True,
        blank=True,
    )
    viewer_ip = models.GenericIPAddressField(_("Viewer IP"), null=True, blank=True)
    last_viewed = models.DateTimeField()

    class Meta:
        verbose_name = _("Content View")
        verbose_name_plural = _("Content Views")
        unique_together = ["content_type", "object_id", "user", "viewer_ip"]

    def __str__(self) -> str:
        return f"{self.content_object} viewed by {self.user.get_full_name if self.user else "Anonymous"} from IP {self.viewer_ip}"

    @classmethod
    def record_view(cls, content_object, user:User, viewer_ip:str) -> None:  # type: ignore
        content_type = ContentType.objects.get_for_model(content_object)
        
        try: 
            view, created = cls.objects.get_or_create(
                content_type=content_type, 
                object_id = content_object.pkid, 
                defaults={"user": user, "viewer_ip": viewer_ip}
            )
            if not created: 
                pass
        except IntegrityError:
            pass