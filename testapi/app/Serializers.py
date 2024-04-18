from app.models import Chat, GPTResponseData
from rest_framework import serializers


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'


class GPTResponseDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = GPTResponseData
        fields = '__all__'
