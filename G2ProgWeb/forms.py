from django.db import models

class cadastro(models.Model):
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    email = models.EmailField()
    data = models.forms.DateField(required=False)