from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from ..models import AI_Recommendation
from ..serializer.aiRecommendationSerializer import AIRecommendationSerializer

class AIRecommendationListView(generics.ListAPIView):
    queryset = AI_Recommendation.objects.all()
    serializer_class = AIRecommendationSerializer
    permission_classes = [IsAuthenticated]

class addAIRecommendation(generics.CreateAPIView):
    queryset = AI_Recommendation.objects.all()
    serializer_class = AIRecommendationSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Associe l'utilisateur connecté au prompt lors de la création
        serializer.save(user=self.request.user)

class getAIRecommendation(generics.RetrieveAPIView):
    queryset = AI_Recommendation.objects.all()
    serializer_class = AIRecommendationSerializer
    permission_classes = [IsAuthenticated]

# Récupérer les recommandations d'IA pour un prompt spécifique
class getAIRecommendationByPrompt(generics.RetrieveAPIView):
    serializer_class = AIRecommendationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        prompt = self.kwargs['prompt']  # Récupère l'ID du prompt dans les paramètres d'URL
        return AI_Recommendation.objects.filter(prompt=prompt)
    
class deleteAIRecommendation(generics.DestroyAPIView):
    queryset = AI_Recommendation.objects.all()
    serializer_class = AIRecommendationSerializer
    permission_classes = [IsAuthenticated]