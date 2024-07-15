#Example 10.20 Google Translate
#pip install googletrans==3.1.0a0

text = "Welcome to London!"

#translates into the mentioned language 
from googletrans import Translator
p = Translator()
# translates the text into german language 
k = p.translate(text,dest='ja')	 
print(k)
