from datetime import date
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.http import JsonResponse

from audit.serializer.promptSerializer import PromptSerializer
from ..serializer.notificationSerializer import NotificationSerializer
from ..serializer.aiRecommendationSerializer import AIRecommendationSerializer
from ..serializer.auditResultSerializer import AuditResultSerializer
from ..serializer.logSerializer import LogSerializer
from ..models import AI_Recommendation, Audit, Prompt
from ..serializer.auditSerializer import AuditSerializer
import os

# Vues d'audit
class AuditListView(generics.ListAPIView):
    queryset = Audit.objects.all()
    serializer_class = AuditSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class getAuditView(generics.RetrieveAPIView):
    queryset = Audit.objects.all()
    serializer_class = AuditSerializer
    permission_classes = [IsAuthenticated]

class getPromptAndAIRecommendationByAudit(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        audit_id = self.kwargs['audit']  # Récupérer l'ID de l'audit depuis l'URL

        # 1. Récupérer le Prompt lié à cet audit
        try:
            prompt = Prompt.objects.get(audit=audit_id)
        except Prompt.DoesNotExist:
            return Response({"error": "Prompt non trouvé pour cet audit"}, status=404)

        # 2. Récupérer l'AI_Recommendation liée au Prompt
        try:
            ai_recommendation = AI_Recommendation.objects.get(prompt=prompt.id)
        except AI_Recommendation.DoesNotExist:
            return Response({"error": "Aucune recommandation IA trouvée pour ce prompt"}, status=404)

        # 3. Sérialiser le Prompt et l'AI_Recommendation
        prompt_serializer = PromptSerializer(prompt)
        ai_recommendation_serializer = AIRecommendationSerializer(ai_recommendation)

        # 4. Retourner une réponse avec les deux sérialiseurs
        return Response({
            "prompt": prompt_serializer.data,
            "ai_recommendation": ai_recommendation_serializer.data
        })

class AuditCreateView(generics.CreateAPIView):
    queryset = Audit.objects.all()
    serializer_class = AuditSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # 1. Sauvegarder l'audit
        audit = serializer.save(user=self.request.user)

        # 2. Récupérer le résultat fourni dans la requête
        result_value = self.request.data.get('result')  # Capturer le champ "result" dans la requête

        if not result_value:
            return Response({"error": "Le champ 'result' est requis"}, status=400)

        # 3. Créer un Audit_Result avec le "result" fourni
        audit_result_data = {
            "audit": audit.id,
            "issues_type": "Initial issues",
            "result": result_value,
            "severity": "Low"
        }
        audit_result_serializer = AuditResultSerializer(data=audit_result_data)
        if audit_result_serializer.is_valid():
            audit_result_serializer.save()

        # 4. Créer un Log
        log_data = {
            "audit": audit.id,
            "timestamp": "2024-10-23T00:00:00Z",
            "log_message": "Audit créé avec succès"
        }
        log_serializer = LogSerializer(data=log_data)
        if log_serializer.is_valid():
            log_serializer.save()

        # 5. Créer un Prompt avec un utilisateur associé
        prompt_data = {
            "audit": audit.id,
            "prompt_text": "Quel est le plan d'action recommandé ?"
        }
        prompt_serializer = PromptSerializer(data=prompt_data)
        if prompt_serializer.is_valid():
            prompt = prompt_serializer.save()  # Sauvegarder le prompt et récupérer l'instance

        # 6. Créer une AI_Recommendation en utilisant l'ID du Prompt créé
        ai_recommendation_data = {
            "prompt": prompt.id,
            "recommendation": "Recommandation initiale basée sur le prompt",
            "applied": False
        }
        ai_recommendation_serializer = AIRecommendationSerializer(data=ai_recommendation_data)
        if ai_recommendation_serializer.is_valid():
            ai_recommendation_serializer.save()
        
         # 7. Créer une notification pour l'utilisateur sans inclure les champs en lecture seule
        notification_data = {
            "type": "Audit",
            "message": "Audit créé avec succès",
            "importance_level": "low"
        }
        notification_serializer = NotificationSerializer(data=notification_data)

        # Vérification de la validation et affichage des erreurs
        if not notification_serializer.is_valid():
            print("Erreurs de validation de NotificationSerializer:", notification_serializer.errors)
        else:
            notification_serializer.save(user=self.request.user, date=date.today())


        # Retourner l'audit créé
        return Response(serializer.data)


class deleteAuditView(generics.DestroyAPIView):
    queryset = Audit.objects.all()
    serializer_class = AuditSerializer
    permission_classes = [IsAuthenticated]

    def perform_destroy(self, instance):
        # Supprimer les Prompt associés
        prompts = instance.prompt_set.all()
        for prompt in prompts:
            # Supprimer les AI_Recommendations associées au prompt
            ai_recommendations = prompt.ai_recommendation_set.all()
            for ai_recommendation in ai_recommendations:
                ai_recommendation.delete()
            prompt.delete()

        # Supprimer les Audit_Result associés
        audit_results = instance.audit_result_set.all()
        for audit_result in audit_results:
            audit_result.delete()

        # Supprimer les Logs associés
        logs = instance.log_set.all()
        for log in logs:
            log.delete()

        # Supprimer l'audit
        instance.delete()

        return JsonResponse({"message": "Audit et tous les éléments associés supprimés avec succès"})
