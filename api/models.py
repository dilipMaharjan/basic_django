from django.conf import settings
from django.db import models

class Employees(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL)
    first_name=models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name