from transformers import pipeline

# Load the summarizer
summarizer = pipeline("summarization")

# Read input text
with open("input.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Summarize
summary = summarizer(text, max_length=150, min_length=40, do_sample=False)

# Print result
print("Summary:\n")
print(summary[0]['summary_text'])
