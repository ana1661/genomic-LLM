from src.fetch_pubmed import fetch_pubmed_abstracts
from src.summarize import summarize_abstracts

if __name__ == "__main__":
    gene = input("Enter a gene or mutation (e.g., TP53): ")
    abstracts = fetch_pubmed_abstracts(gene)
    if abstracts:
        summary = summarize_abstracts(abstracts, gene)
        print("\n--- Summary ---\n")
        print(summary)
    else:
        print("No abstracts found.")