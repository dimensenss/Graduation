from django.contrib.auth.models import User
from django.db import models


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    is_instructor = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
