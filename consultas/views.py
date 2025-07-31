from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Consulta, Medico, Paciente
from .serializers import ConsultaSerializer, PacienteSerializer, MedicoSerializer
from django_filters.rest_framework import DjangoFilterBackend

class ConsultaViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated] 
    queryset = Consulta.objects.all().order_by('-data_hora')
    serializer_class = ConsultaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['paciente', 'medico', 'status']

class MedicoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer

class PacienteViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
