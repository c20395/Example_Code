# Example 10.34 Text Generation with transformers (GPT-2 Model)
# pip install transformers
from transformers import pipeline, set_seed
generator = pipeline('text-generation', model='gpt2')
set_seed(20)
generator("I feel amazing about", max_length=20, num_return_sequences=5)
