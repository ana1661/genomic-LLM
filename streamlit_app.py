import streamlit as st
from src.fetch_pubmed import fetch_pubmed_abstracts
from src.summarize import summarize_abstracts
import torch
import streamlit as st

# Detect device
device_status = "Running on GPU ✅" if torch.cuda.is_available() else "Running on CPU ❌"

# Show device status on sidebar
st.sidebar.markdown(f"### {device_status}")


st.title("Genomic Literature Assistant")

st.write("Enter a gene name (example: TP53) and I will summarize recent research articles for you!")

gene = st.text_input("Enter gene name or mutation")

if st.button("Fetch Summary"):
    if gene:
        with st.spinner(f"Fetching PubMed abstracts for {gene}..."):
            abstracts = fetch_pubmed_abstracts(gene, max_results=3)

        if abstracts:
            with st.spinner("Summarizing abstracts..."):
                summary = summarize_abstracts(abstracts, gene)
            st.success("Here is your genomic literature summary:")
            st.write(summary)
        else:
            st.error("No abstracts found for this gene or mutation. Please try a different one.")
    else:
        st.error("Please enter a gene name first!")

