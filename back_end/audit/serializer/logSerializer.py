from rest_framework import serializers
from ..models import Log

class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = ['id', 'audit', 'timestamp', 'log_message']
