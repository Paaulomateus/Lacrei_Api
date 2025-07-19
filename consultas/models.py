from django.db import models

# Create your models here.

class Consulta(models.Model):
    STATUS_CHOICES = [
        ('AG', 'Agendada'),
        ('CN', 'Cancelada'),
        ('RF', 'Reagendada'),
        ('FN', 'Finalizada'),
    ]

    paciente = models.CharField(max_length=150)
    medico = models.CharField(max_length=150)
    data_hora = models.DateTimeField()
    motivo = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='AG')
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.paciente} com {self.medico} em {self.data_hora.strftime('%d/%m/%Y %H:%M')} - {self.get_status_display()}"