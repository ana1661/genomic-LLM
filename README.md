# Genomic Literature Assistant

A Streamlit-based web app that fetches recent PubMed abstracts for a gene or mutation (e.g. TP53) and summarizes them using an LLM. Designed for researchers, students, and healthcare professionals who need fast insights into biomedical literature.

---

##  Features

- Fetches top PubMed abstracts based on gene name
- Summarizes using BioGPT-Large (or BART for fast mode)
- Streamlit frontend with clean UI
- GPU-ready (can run locally with Docker + CUDA)
- Detects and displays GPU/CPU mode

---

## Run Locally

```bash
git clone https://github.com/ana1661/genomic-LLM.git
cd genomic-LLM

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run streamlit_app.py
