# Example 4.23
# https://github.com/huggingface/transformers
# pip install transformers
# https://aka.ms/vs/16/release/vc_redist.x64.exe


from transformers import pipeline
classifier = pipeline('sentiment-analysis')
classifier('This is a good movie.')
