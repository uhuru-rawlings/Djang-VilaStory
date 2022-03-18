from django.db import models
from profiles.models import Profiles
# Create your models here.
class ImportantInfo(models.Model):
    village = models.ForeignKey(Profiles, on_delete = models.CASCADE)
    hospital = models.CharField(max_length=300)
    policestation = models.CharField(max_length=300)
    market = models.CharField(max_length=300)