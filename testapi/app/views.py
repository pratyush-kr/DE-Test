from rest_framework import viewsets, status
from testapi.ManualRequest import ManualRequest
from testapi.settings import PROMPT
from app.Services import generate_prompt, automated_test
from rest_framework.decorators import action
from rest_framework.response import Response
from app.models import Chat, User, Demo
from app.Serializers import ChatSerializer, UserSerializer, DemoSerializer
from app.models import GPTResponseData
from django.views.decorators.csrf import csrf_exempt
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
        gpt_response = GPTResponseData.objects.create()
        gpt_response.message = res
        gpt_response.save()
        matches = re.findall(r'```json\n(.+)```\n', res, flags=re.DOTALL | re.MULTILINE)
        data = dict()
        for match in matches:
            array = json.loads(re.sub(r"//.+?\n", "", match))
            i = 1
            for element in array:
                element['testCases'] = f"Test Case {i} {element['testCases']}"
                i += 1
            data = array
        if request.headers['scenario'] == "automatic":
            res = automated_test(data, userView=UserView())
            return Response(res, status=status.HTTP_200_OK)
        return Response({"requests": data}, status=status.HTTP_200_OK)


class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    @action(methods=["POST"], detail=False)
    def login(self, request):
        username = request.data['username']
        password = request.data['password']
        # address = request.data['address']
        # job_desc = request.data['jobDesc']
        user = User.objects.get(username=username)
        if user is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"data": "Login Successful"}, status=status.HTTP_200_OK)


class DemoView(viewsets.ModelViewSet):
    serializer_class = DemoSerializer
    queryset = Demo.objects.all()

    @csrf_exempt
    @action(methods=["POST"], detail=False)
    def test_requests(self, request):
        requests_list = request.data['requests']
        response = []
        userView = UserView()
        manualRequest = ManualRequest()
        i = 1
        for req in requests_list:
            data = dict()
            data['scenario'] = req['testCases']
            data['request'] = req['payload']
            manualRequest.data = req['payload']
            try:
                res = userView.login(manualRequest)
                data['response'] = res.data
            except Exception as e:
                data['response'] = {"error": f'API failed with error: {e}'}
            response.append(data)
            i += 1
        return Response({"data": response}, status=status.HTTP_200_OK)
