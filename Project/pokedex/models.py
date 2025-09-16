from django.db import models

# Create your models here.

class Pokemon (models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    nome = models.CharField(max_length=255)
    altura = models.IntegerField()
    imagem = models.CharField(max_length=500)

    def __str__(self):
        return self.nome