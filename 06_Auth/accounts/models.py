from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

# 유저 정보를 담는 모델 클래스만을 위한 모델클래스가 이미 존재한다.
# models.Model은 범용적은 모델 클래스를 정의하기 위한 클래스다.
# 따라서 models의 Model 클래스말고 AbstractUser를 사용한다.
class User(AbstractUser):
    pass