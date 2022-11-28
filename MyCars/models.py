from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Cars(models.Model):
    modelo = models.CharField(
        max_length=100, help_text='Digite o Modelo')
    marca = models.TextField(
        help_text='Digite a marca')
    valor = models.DecimalField(decimal_places=2, help_text='Digite o valor', max_digits=9)
    observacoes = models.TextField(
        help_text='Digite as Observações'
    )
    fotos = models.ImageField(upload_to='MyCars/static/MyCars/img', null=True)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    