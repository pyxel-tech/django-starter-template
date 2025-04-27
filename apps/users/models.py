from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    picture = models.ImageField('Imagem de usuário', blank=True, null=True)

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
