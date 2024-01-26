import openai


def call_openai(message):
    print("Getting summary for: " + message)

    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {
                "role": "assistant",
                "content": f"{message}"
            }
        ]
    )
    print(completion.choices[0].message.content)

    return completion.choices[0].message.content


if __name__ == "__main__":
    call_openai('Co Fredro miał na myśli pisząc: "kończ waść, wstydu oszczędź?"')
