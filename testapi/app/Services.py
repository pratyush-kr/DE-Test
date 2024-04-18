import openai


def generate_prompt(prompt_):
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=prompt_,
        max_tokens=4096,
        stop="bye"
    )
    return response.choices[0]['message']['content']
