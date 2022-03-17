from django.db import models

# Create your models here.
class Signups(models.Model):
    useremail = models.EmailField(max_length=200)
    phone = models.CharField(max_length=200)
    village = models.CharField(max_length=200)
    passwords = models.CharField(max_length=300)

    class Meta:
        db_table = 'Signups'

    def __str__(self):
        return self.useremail