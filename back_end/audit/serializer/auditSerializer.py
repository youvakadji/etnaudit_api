from rest_framework import serializers
from ..models import Audit

class AuditSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)  # Utiliser PrimaryKeyRelatedField pour les clés étrangères

    class Meta:
        model = Audit
        fields = ['id', 'user', 'type', 'status', 'score', 'createdAt']
