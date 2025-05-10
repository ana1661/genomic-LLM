'''
from transformers import pipeline

# Load the summarization pipeline (you can change the model here)
summarizer = pipeline("summarization", model="facebook/bart-large-cnn", device=0)

def summarize_abstracts(abstracts, gene_name):
    combined_text = "\n\n".join(abstracts)

    # Hugging Face models usually have a 1024 token limit. We'll chunk if needed.
    chunks = [combined_text[i:i+1000] for i in range(0, len(combined_text), 1000)]

    summaries = []
    for chunk in chunks:
        summary = summarizer(chunk, max_length=300, min_length=60, do_sample=False)
        summaries.append(summary[0]["summary_text"])

    # Return joined summary
    return f"Summary for {gene_name}:\n\n" + "\n\n".join(summaries)
'''
# src/summarize.py

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

device = 0 if torch.cuda.is_available() else -1

tokenizer = AutoTokenizer.from_pretrained("microsoft/BioGPT-Large")
model = AutoModelForCausalLM.from_pretrained("microsoft/BioGPT-Large")

if device == 0:
    model = model.to('cuda')

generator = pipeline("text-generation", model=model, tokenizer=tokenizer, device=device)

def summarize_abstracts(abstracts, gene_name):
    text = "\n\n".join(abstracts)

    # Safety: limit input text length
    if len(text.split()) > 500:  # if more than 500 words
        text = " ".join(text.split()[:500])  # truncate to 500 words

    prompt = f"Summarize the following PubMed abstracts about the gene {gene_name}:\n\n{text}\n\nSummary:"

    outputs = generator(
        prompt,
        max_new_tokens=200,  # generate 200 tokens max
        do_sample=True,
        top_k=50,
        top_p=0.95
    )
    return outputs[0]["generated_text"]
