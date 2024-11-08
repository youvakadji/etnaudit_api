from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from ..models import Audit_Result
from ..serializer.auditResultSerializer import AuditResultSerializer

class AuditResultListView(generics.ListAPIView):
    queryset = Audit_Result.objects.all()
    serializer_class = AuditResultSerializer
    permission_classes = [IsAuthenticated]

class saveResultView(generics.CreateAPIView):
    queryset = Audit_Result.objects.all()
    serializer_class = AuditResultSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Associe l'utilisateur connecté au résultat lors de la création
        serializer.save(user=self.request.user)

class getAuditResultView(generics.RetrieveAPIView):
    queryset = Audit_Result.objects.all()
    serializer_class = AuditResultSerializer
    permission_classes = [IsAuthenticated]

class getAuditResultByAuditIdView(generics.ListAPIView):
    serializer_class = AuditResultSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        audit_id = self.kwargs['audit_id']
        return Audit_Result.objects.filter(audit_id=audit_id)

class deleteAuditResultView(generics.DestroyAPIView):
    queryset = Audit_Result.objects.all()
    serializer_class = AuditResultSerializer
    permission_classes = [IsAuthenticated]