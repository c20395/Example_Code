# Example 4.20 The Gensim.py Program
# https://radimrehurek.com/gensim/
# pip install gensim
from gensim.summarization import summarize
# How to create a dictionary from a list of sentences?
text ='''
  Artificial intelligence (AI), is intelligence demonstrated by machines, 
  unlike the natural intelligence displayed by humans and animals. 
  Leading AI textbooks define the field as the study of "intelligent agents": 
  any device that perceives its environment and takes actions that maximize its 
  chance of successfully achieving its goals.[3] Colloquially, the term 
  "artificial intelligence" is often used to describe machines (or computers) 
  that mimic "cognitive" functions that humans associate with the human mind, 
  such as "learning" and "problem solving".[4]
'''

print(summarize(text, ratio = 0.5))
from gensim.summarization import keywords
print(keywords(text))

