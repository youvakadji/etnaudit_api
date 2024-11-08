from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from ..serializer.promptSerializer import PromptSerializer
from ..models import Prompt


class PromptListView(generics.ListAPIView):
    queryset = Prompt.objects.all()
    serializer_class = PromptSerializer
    permission_classes = [IsAuthenticated]

class getPromptView(generics.RetrieveAPIView):
    queryset = Prompt.objects.all()
    serializer_class = PromptSerializer
    permission_classes = [IsAuthenticated]

class getPromptByAudit(generics.RetrieveAPIView):
    serializer_class = PromptSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        audit = self.kwargs['audit']  # Récupère l'ID de l'audit dans les paramètres d'URL
        return Prompt.objects.filter(audit=audit)

class addPromptView(generics.CreateAPIView):
    queryset = Prompt.objects.all()
    serializer_class = PromptSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Associe l'utilisateur connecté au prompt lors de la création
        serializer.save(user=self.request.user)

class deletePromptView(generics.DestroyAPIView):
    queryset = Prompt.objects.all()
    serializer_class = PromptSerializer
    permission_classes = [IsAuthenticated]