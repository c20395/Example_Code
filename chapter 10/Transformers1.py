# Example 10.31 Sentiment analylsis with transformers
# https://github.com/huggingface/transformers 
from transformers import pipeline

# Allocate a pipeline for sentiment-analysis
classifier = pipeline('sentiment-analysis')
classifier('We are very happy to visit London.')
