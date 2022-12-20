# from rest_framework import serializers
# from .models import Test
from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = "__all__"
# class TestSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Test
#         fields = ['email', 'password']