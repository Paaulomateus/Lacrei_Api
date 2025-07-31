from django.db import models

# Create your models here.

class Consulta(models.Model):
    STATUS_CHOICES = [
        ('AG', 'Agendada'),
        ('CN', 'Cancelada'),
        ('RF', 'Reagendada'),
        ('FN', 'Finalizada'),
    ]

    paciente = models.ForeignKey('Paciente', on_delete=models.CASCADE, related_name='consultas')
    medico = models.ForeignKey('Medico', on_delete=models.CASCADE, related_name='consultas')
    data_hora = models.DateTimeField()
    motivo = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='AG')
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.paciente.nome} com {self.medico.nome} em {self.data_hora.strftime('%d/%m/%Y %H:%M')} - {self.get_status_display()}"


class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=11, unique=True)

    def __str__(self):
        return self.nome

class Medico(models.Model):
    nome = models.CharField(max_length=100)
    crm = models.CharField(max_length=10, unique=True)
    especialidade = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    
