from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    """
    Currently unused in preference of the below.
    """
    email = serializers.EmailField(
        required=True
    )
    first_name = serializers.CharField(max_length=52, required=False)
    last_name = serializers.CharField(max_length=52, required=False)
    password = serializers.CharField(min_length=8, write_only=True)
    username = serializers.CharField(max_length=26, required=True)
    fav_color = serializers.CharField(required=False)

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password', 'first_name', 'last_name', 'fav_color')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = CustomUser(**validated_data)
        # instance = self.Meta.model(**validated_data)  # as long as the fields are the same, we can just use this
        if password is not None:
            instance.set_password(password)  # creates a hash for password
        instance.save()
        return instance


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)  # Python 3 syntax

        # token = super(MyTokenObtainPairSerializer, cls).get_token(user) # Python 2 and earlier
        # Add custom claims
        token['fav_color'] = user.fav_color
        return token
