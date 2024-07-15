# Example 10.2
# pip install spacy
# python -m spacy download en_core_web_sm
# https://aka.ms/vs/16/release/vc_redist.x64.exe

import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from collections import Counter
from heapq import nlargest

#nlp = spacy.load('en')
nlp = spacy.load('en_core_web_sm')

introduction_text = ('London is the capital of the UK,'
                     ' with a population of nearly 9 millions people.'
                     ' London is one of the most diverse cities in the world.'
                     ' London has over 100 museums, galleries and exhibitions.'
                     ' London has 40 universities and higher education institutions.'
                     ' London has over 15,500 restaurants, serving Italian, Indian, Thai and Chinese cuisines.'
                     ' London is also one of the world''s capitals of finance, fashion, arts and entertainment.')

doc = nlp(introduction_text)

print("1. Keywords ==============================================")
keyword = []
stopwords = list(STOP_WORDS)
pos_tag = ['PROPN','ADJ','NOUN','VERB']
for token in doc:
     if(token.text in stopwords or token.text in punctuation):
          continue
     if(token.pos_ in pos_tag):
          keyword.append(token.text)
print(keyword)

freq_word = Counter(keyword)
print(freq_word.most_common(5))

print("2. Sentence Strength =====================================")
sent_strength = {}
for sent in doc.sents:
     for word in sent:
          if word.text in freq_word.keys():
               if sent in sent_strength.keys():
                    sent_strength[sent]+=freq_word[word.text]
               else:
                    sent_strength[sent]=freq_word[word.text]
print(sent_strength)

print("6. Summary ===============================================")
summerized_sentences = nlargest(3,sent_strength,key=sent_strength.get)
print(summerized_sentences)
                    
