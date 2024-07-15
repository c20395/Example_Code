# Example 10.5: Summarize Wiki page with gensim
#!pip install wikipedia

from gensim.summarization.summarizer import summarize 
from gensim.summarization import keywords 
import wikipedia 
  
wikisearch = wikipedia.page("Artificial_intelligence") 
wikicontent = wikisearch.content 
  
# Save the content to a text file 
with open("wiki.txt", 'w', encoding='utf-8') as f:
    print(wikicontent, file=f)  

from smart_open import smart_open
text = " ".join((line for line in smart_open('wiki.txt', encoding='utf-8')))

# Summary (0.5% of the original content). 
summ = summarize(text, ratio = 0.05) 
print(summ)
