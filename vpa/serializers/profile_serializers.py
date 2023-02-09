from django.contrib.auth.models import User
from rest_framework import serializers


class ProfileModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')
