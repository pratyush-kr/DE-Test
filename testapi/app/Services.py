import openai


def generate_prompt(prompt_):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=prompt_,
        max_tokens=1500,
        stop="bye"

    )
    return response.choices[0]['message']['content']
