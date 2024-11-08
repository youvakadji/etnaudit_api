from rest_framework import serializers
from ..models import AI_Recommendation

class AIRecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AI_Recommendation
        fields = ['id', 'prompt', 'recommendation', 'applied']
