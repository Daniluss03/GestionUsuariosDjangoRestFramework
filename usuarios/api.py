from rest_framework import viewsets, permissions
from .models import Role
from .serializers import RoleSerializer

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [permissions.AllowAny]  # Permitir cualquier usuario acceder a la API
