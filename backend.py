import openai


class ChatBot:
    def __init__(self):
        openai.api_key = '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'

    def get_response(self, user_input):
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=user_input,
            max_tokens=4000,
            temperature=0.5
        ).choices[0].text
        return response


if __name__ == '__main__':
    chatbot = ChatBot()
    response = chatbot.get_response('Write a joke about birds.')
    print(response)
