# Example 10.4: Summarize Wiki page with gensim
#!pip install wikipedia

from gensim.summarization.summarizer import summarize 
from gensim.summarization import keywords 
import wikipedia 
  
wikisearch = wikipedia.page("Artificial_intelligence") 
wikicontent = wikisearch.content 
  
# Summary (0.5% of the original content). 
summ = summarize(wikicontent, ratio = 0.05) 
print(summ)
