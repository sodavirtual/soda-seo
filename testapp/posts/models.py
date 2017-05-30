from django.db import models


class Post(models.Model):

    title = models.CharField(
        'título',
        max_length=255
    )

    body = models.TextField(
        'conteúdo'
    )

    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    def __str__(self):
        return self.title
