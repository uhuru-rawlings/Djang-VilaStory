from django.db import models
from signups.models import Signups

# Create your models here.
class Profiles(models.Model):
    users = models.ForeignKey(Signups, on_delete = models.CASCADE)
    userimages = models.ImageField(upload_to = 'profiles/')
    aboutme = models.TextField()

    class Meta:
        db_table = 'Profiles'

    def __str__(self):
        return self.aboutme

class Posts(models.Model):
    postby = models.ForeignKey(Signups, on_delete = models.CASCADE)
    post_image = models.ImageField(upload_to = 'posts/', null = True)
    post_text = models.TextField()
    post_dates = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Posts'

    def __str__(self):
        return self.post_text