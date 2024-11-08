from rest_framework import serializers
from ..models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ['id', 'username', 'email','password']  # Ajout du champ password

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)  # Extraire le mot de passe des données validées
        user = super().update(instance, validated_data)  # Mettre à jour les autres champs
        
        if password:
            user.set_password(password)  # Hash le nouveau mot de passe
            user.save()  # Sauvegarder l'utilisateur avec le mot de passe mis à jour

        return user

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        return user
    

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email and password:
            try:
                # Récupérer l'utilisateur via l'email
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                raise serializers.ValidationError("L'email ou le mot de passe est incorrect.")

            # Utiliser l'authentification avec email et mot de passe
            user = authenticate(username=user.username, password=password)

            if user is None:
                raise serializers.ValidationError("L'email ou le mot de passe est incorrect.")

            if not user.is_active:
                raise serializers.ValidationError("Ce compte est désactivé.")

            # Générer les tokens JWT
            tokens = RefreshToken.for_user(user)
            return {
                'email': user.email,
                'access': str(tokens.access_token),
                'username': user.username,
            }
        else:
            raise serializers.ValidationError("Doit inclure l'email et le mot de passe.")