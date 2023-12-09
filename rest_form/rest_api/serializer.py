from rest_api.models import *
from rest_framework import serializers


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = "__all__"