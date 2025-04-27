from django.contrib.auth.models import AbstractUser
from django.db import models
from shared.models import BaseModel


class User(AbstractUser):
    picture = models.ImageField('Imagem de usuário',
                                upload_to='users/pictures',
                                blank=True,
                                null=True)

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'


class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Perfil do usuário'
        verbose_name_plural = 'Perfis do usuário'

    def __str__(self):
        return self.user.username
