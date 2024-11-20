from django.db import models
from django.utils.timezone import now

# Assinatura de E-mail
class EmailSubscription(models.Model):
    email = models.EmailField(unique=True, verbose_name="E-mail")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Data de Atualização")

    def __str__(self):
        return self.email

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    idade = models.IntegerField()

