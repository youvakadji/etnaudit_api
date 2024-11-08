from rest_framework import serializers
from ..models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)  # Utiliser PrimaryKeyRelatedField pour les clés étrangères

    class Meta:
        model = Notification
        fields = ['id', 'user', 'date', 'type', 'message', 'importance_level']  # Inclure tous les champs nécessaires
        read_only_fields = ['user']  # Le champ user est en lecture seule
