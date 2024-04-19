import openai
from testapi import ManualRequest


def generate_prompt(prompt_):
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=prompt_,
        max_tokens=4096,
        stop="bye"
    )
    return response.choices[0]['message']['content']


def automated_test(data, userView=None):
    requests_list = data
    response = []
    manualRequest = ManualRequest
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
    return response
