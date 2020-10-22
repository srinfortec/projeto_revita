from django.db import models

# Create your models here.


class HorarioDisponivel(models.Model):

    dia_semana = models.DateField(
        null=False,
        blank=False
    )

    horario = models.CharField(
        max_length=255,
        blank=False,
        null=False
    )

class Clientes (models.Model):

    nome_completo = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    data_nascimento = models.DateField(
        null=False,
        blank=False
    )

    endereco = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    whatsapp = models.CharField(
        max_length=11,
        null=False,
        blank=False
    )

    email = models.CharField(
        max_length=50,
        null=False,
        blank=False
    )
    problema = models.TextField(
        blank= True
    )
    horario_disponivel= models.ForeignKey(HorarioDisponivel, on_delete=models.CASCADE, null=True)


