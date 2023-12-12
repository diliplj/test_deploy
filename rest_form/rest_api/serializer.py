from rest_api.models import *
from rest_framework import serializers


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = "__all__"

    # def validate(self, data):
    #     pass

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(label="Email address", max_length=57, required=True)
    password = serializers.CharField(max_length = 200, required=True)