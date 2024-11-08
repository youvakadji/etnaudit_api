from rest_framework import serializers
from ..models import Audit_Result

class AuditResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audit_Result
        fields = ['id', 'audit', 'issues_type', 'result', 'severity']
