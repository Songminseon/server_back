from rest_framework import serializers
from .models import PhoneBook

class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'name',
            'phone',
        )
        model = PhoneBook