# Example 10.29 Chatterbot basic demo
# https://chatterbot.readthedocs.io/en/stable/setup.html
# https://chatterbot.readthedocs.io/en/stable/examples.html

# pip install spacy
# pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.2.0/en_core_web_sm-2.2.0.tar.gz
# python -m spacy download en
# pip install chatterbot_corpus

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('Ron Obvious')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the english corpus
trainer.train("chatterbot.corpus.english")

# Get a response to an input statement
#chatbot.get_response("Hello, how are you today?")

while True:
    message = input('You:')
    if message.strip()!= 'Bye':
        reply = chatbot.get_response(message)
    print('ChatBot:',reply)
    if message.strip()=='Bye':
        print('ChatBot:Bye')
        break
