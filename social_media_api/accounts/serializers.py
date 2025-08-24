from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "bio", "profile_picture"]


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "password", "token"]

    def create(self, validated_data):
        # ✅ Create user
        user = get_user_model().objects.create_user(
            username=validated_data["username"],
            email=validated_data.get("email"),
            password=validated_data["password"]
        )
        # ✅ Create token
        token, _ = Token.objects.get_or_create(user=user)
        # attach token so it's returned in response
        user.token = token.key
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    token = serializers.CharField(read_only=True)

    def validate(self, data):
        user = authenticate(
            username=data["username"], password=data["password"])
        if not user:
            raise serializers.ValidationError("Invalid credentials")
        token, _ = Token.objects.get_or_create(user=user)
        return {"user": user, "token": token.key}
