from rest_api.models import *
from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','email','password')

    # def validate(self, data):
    #     print("validate coming",data)
    #     password = data.get('password')
    #     error = password_validator(password)
    #     if error:
    #         raise serializers.ValidationError(error)
    #     else:
    #         return data
        

class LoginSerializer(serializers.Serializer):
    username = serializers.EmailField(label="username", max_length=57, required=True)
    password = serializers.CharField(label = "password",max_length = 200, required=True)
