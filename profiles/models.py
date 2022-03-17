from django.db import models
from signups.models import Signups

# Create your models here.
class Profiles(models.Model):
    users = models.ForeignKey(Signups, on_delete = models.CASCADE)
    userimages = models.ImageField()