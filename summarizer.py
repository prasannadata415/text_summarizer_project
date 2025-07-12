from transformers import pipeline

# Load the summarizer model only once
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def generate_summary(text, max_length=150, min_length=40):
    summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
    return summary[0]['summary_text']
