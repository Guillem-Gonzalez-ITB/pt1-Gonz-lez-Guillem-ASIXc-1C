import requests


def get_data__from_keyboard():
    sentence = input("Introduce una frase: ")
    return sentence


def get_data_from_server():
    response = requests.models.Response()
    while response.status_code != requests.codes.ok:
        your_api_key = ""
        api_url = 'https://api.api-ninjas.com/v1/chucknorris'
        response = requests.get(api_url, "joke", headers={'X-Api-Key': your_api_key})

        if response.status_code == requests.codes.ok:
            sentence = (response.text[10:-2])
            return sentence

        else:
            print("Error:", response.status_code, response.text)


def get_data_from_file():
    print("Aplicable en la tercera entrega.")
    exit()


def get_data_from_chatgpt():
    your_api_key = ""
    prompt_text = input("Introduce un texto: ")
    api_url = "https://api.openai.com/v1/chat/completions"

    headers = {
        "Content-Type": "text",
        "Authorization": f"Bearer {your_api_key}"
    }

    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are a gpt-3.5-turbo chatbot."},
            {"role": "user", "content": prompt_text},
            {"role": "assistant", "content": "Aqui tienes tu respuesta: "}
        ],
        "max_tokens": 255,
    }

    response = requests.post(api_url, headers=headers, params=data)

    if response.status_code == 200:
        sentence = response.json()
        print("Completion:", sentence['choices'][0]['text'])
    else:
        print("Error:", response.text)

    print("sinceramente se hizo lo que se pudo")
