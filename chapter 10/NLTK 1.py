# Example 10.10 NLTK example with wordcloud
# pip install wordcloud

#Open the text file :
text_file = open("london.txt")

#Read the data :
text = text_file.read()

#Import required libraries :
import nltk
from nltk import sent_tokenize
from nltk import word_tokenize

import nltk
nltk.download("popular")

#Tokenize the text by sentences :
sentences = sent_tokenize(text)

#How many sentences are there? :
print (len(sentences))

#Print the sentences :
print(sentences)

#Tokenize the text with words :
words = word_tokenize(text)

#Print words :
print (words)

#Import required libraries :
from nltk.probability import FreqDist

#Find the frequency :
fdist = FreqDist(words)

#Print 10 most common words :
print(fdist.most_common(10))

#Library to form wordcloud :
from wordcloud import WordCloud
import matplotlib.pyplot as plt
wordcloud = WordCloud().generate(text)

#Plot the wordcloud :
plt.figure(figsize = (12, 12)) 
plt.imshow(wordcloud) 

#To remove the axis value :
plt.axis("off") 
plt.show()
