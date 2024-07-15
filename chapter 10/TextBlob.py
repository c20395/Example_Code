#Example 10.6 TextBlob
# https://textblob.readthedocs.io/en/dev/
#!pip install textblob
#!pip install nltk 
#!python -m textblob.download_corpora

from textblob import TextBlob

text = '''
Artificial intelligence (AI), is intelligence demonstrated by machines, 
  unlike the natural intelligence displayed by humans and animals. 
  Leading AI textbooks define the field as the study of "intelligent agents": 
  any device that perceives its environment and takes actions that maximize its 
  chance of successfully achieving its goals.[3] Colloquially, the term 
  "artificial intelligence" is often used to describe machines (or computers) 
  that mimic "cognitive" functions that humans associate with the human mind, 
  such as "learning" and "problem solving".[4]
'''

blob = TextBlob(text)
print(blob.tags)          
print(blob.noun_phrases)   

#Tokenization
print(blob.words)
print(blob.sentences)

#Sentiment Analsys
blob = TextBlob("This is a cool gadget!")
print(blob.sentiment)
blob = TextBlob("I am not really interested!")
print(blob.sentiment)
