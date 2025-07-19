from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ConsultaViewSet, MedicoViewSet, PacienteViewSet

router = DefaultRouter()
router.register(r'consultas', ConsultaViewSet)
router.register(r'medicos', MedicoViewSet)
router.register(r'pacientes', PacienteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

