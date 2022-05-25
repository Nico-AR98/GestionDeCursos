from django.db import models

# Create your models here.
class Curso(models.Model):
    codigo= models.CharField(primary_key=True,max_length=6)
    nombre= models.CharField(max_length=58)
    creditos = models.PositiveSmallIntegerField()

    def __str__(self):
        txt = "({0}) {1}"
        return txt.format(self.codigo,self.nombre)

