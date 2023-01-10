from django.db import models

class Exptedientes(models.Model):
    Exptediente = models.CharField(max_length=20)
    Nombre_Causante = models.CharField(max_length=20)
    Apellido_Causante = models.CharField(max_length=20) 
    DNI = models.CharField(max_length=10)
    
    def __srt__(self):
        return f"{self.Expediente}, {self.Nombre_Causante}, {self.Apellido_Causante}, {self.DNI}"
