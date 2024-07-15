# Example 10.33 open question answering with transformers
from transformers import pipeline

context = '''
We created Biox Systems Ltd company back in the year of 2000.
'''
Question = input('Ask a question:')
question_answerer = pipeline('question-answering')
result = question_answerer(question=Question, context=context)
print("Answer:", result['answer'])
print("Score:", result['score'])
