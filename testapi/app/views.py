from rest_framework import viewsets, status
from testapi.settings import PROMPT
from app.Services import generate_prompt
from rest_framework.decorators import action
from rest_framework.response import Response
from app.models import Chat
from app.Serializers import ChatSerializer
from app.models import GPTResponseData
import re
import json


class ChatView(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

    @action(methods=["POST"], detail=False)
    def get_test_cases(self, request):
        message = request.data['request']
        print(message)
        prompt = [PROMPT]
        query = message
        prompt += [{"role": "user", "content": f'{query}'}]
        res = generate_prompt(prompt)
        matches = re.findall(r'```json\n(.+)```\n', res, flags=re.DOTALL | re.MULTILINE)
        data = dict()
        for match in matches:
            data['response'] = json.loads(match)
            gpt_response = GPTResponseData.objects.create()
            gpt_response.message = match
            gpt_response.save()

        return Response(data, status=status.HTTP_200_OK)
