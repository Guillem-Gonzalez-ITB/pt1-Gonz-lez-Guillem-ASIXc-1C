import requests


def get_data__from_keyboard():
    sentence = input("Introduce una frase: ")
    return sentence


def get_data_from_server(URL):
    sentence = requests.get(URL)
    return sentence.text


def get_data_from_chatGPT(questio):
    sentence = requests.post("https://api.openai.com/v1/engines/davinci-codex/completions",
                            headers={question: questio},
