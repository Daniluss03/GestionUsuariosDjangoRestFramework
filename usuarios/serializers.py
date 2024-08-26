from rest_framework import serializers
from .models import Role

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'name', 'is_active', 'Roles', 'created_at']
        read_only_fields = ['created_at',]
