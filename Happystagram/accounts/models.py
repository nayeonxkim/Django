from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

def articles_image_path(instance, filename):
    return f'articles/{instance.user.username}/images/{filename}'


# Create your models here.
class User(AbstractUser):
    pass

class Profile(models.model):
    nickname = models.CharField(max_length=40, blank=True)
    introduction = models.TextField(blank=True)
    image_file = ProcessedImageField(upload_to=articles_image_path,
                                     processors=[ResizeToFill(300, 300)],
                                     format='JPEG',
                                     options={'quality': 90})
    user = models.ForeignKey(User, on_delete=models.CASCADE)