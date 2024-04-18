from rest_framework import viewsets, status
from testapi.settings import PROMPT
from app.Services import generate_prompt
from rest_framework.decorators import action
from rest_framework.response import Response
from app.models import Chat
from app.Serializers import ChatSerializer


class ChatView(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

    @action(methods=["POST"], detail=False)
    def get_test_cases(self, request):
        message = request.data['message']
        print(message)
        prompt = [PROMPT]
        query = message
        prompt += [{"role": "user", "content": query}]
        res = generate_prompt(prompt)
        print(res)
        return Response({'message': res}, status=status.HTTP_200_OK)
