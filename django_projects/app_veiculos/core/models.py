import datetime
from django.db import models


class Fabricante(models.Model):
  nome = models.CharField(max_length=100)
  pais = models.CharField(max_length=50, null=True, blank=True)
  ano_fundacao = models.PositiveIntegerField(null=True, blank=True)

  def __str__(self):
    return self.nome
  
  def idade(self):
    return datetime.date.today().year - self.ano_fundacao
  

MOTOR_CHOICES = (
  ("1.0", "Motor 1.0"),
  ("1.3", "Motor 1.3"),
  ("1.4", "Motor 1.4"),
  ("1.6", "Motor 1.6"),
  ("1.8", "Motor 1.8"),
  ("2.0", "Motor 2.0"),
)

class Modelo(models.Model):
  nome = models.CharField(max_length=100)
  motor = models.CharField(choices=MOTOR_CHOICES, max_length=5, null=True, blank=True)
  
  fabricante = models.ForeignKey(Fabricante, 
                                 on_delete=models.RESTRICT,
                                 related_name='modelos')
  
  def __str__(self):
    return self.nome
