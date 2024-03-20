import requests



client = openai.OpenAI()
questio = input("Introduce una frase: ")
sentence = requests.post("https://api.openai.com/v1/chat/completions", client.chat.completions.create(
    model="gpt-3.5-turbo",
    response_format={type: "string"},
    messages={"role": "user", "content": questio}

))

print()