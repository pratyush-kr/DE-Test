from app.models import Chat, GPTResponseData, User, Demo
from rest_framework import serializers


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'


class GPTResponseDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = GPTResponseData
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class DemoSerializer(serializers.Serializer):
    class Meta:
        model = Demo
        fields = '__all__'
