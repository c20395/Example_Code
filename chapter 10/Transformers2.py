# Example 10.32 Q&A with transformers
from transformers import pipeline
question_answerer = pipeline('question-answering')
question_answerer({
     'question': 'What is the name of the company?',
     'context': 'We created Biox Systems Ltd company back in the year of 2000.'
})
