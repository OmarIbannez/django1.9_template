from django.db import models
from config.settings import AUTH_USER_MODEL


class BaseModel(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(blank=True, default=False)

    class Meta:
        abstract = True
