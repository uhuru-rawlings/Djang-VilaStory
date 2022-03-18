from django.db import models
from profiles.models import Profiles
from signups.models import Signups
# Create your models here.
class ImportantInfo(models.Model):
    village = models.CharField(max_length=200)
    hospital = models.CharField(max_length=300)
    policestation = models.CharField(max_length=300)
    market = models.CharField(max_length=300)

    class Meta:
        db_table = 'ImportantInfo'

    def __str__(self):
        return self.hospital