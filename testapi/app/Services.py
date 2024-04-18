import openai


def generate_prompt(prompt_):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=prompt_,
        max_tokens=150,
        stop="bye"

    )
    return response.choices[0]['message']['content']