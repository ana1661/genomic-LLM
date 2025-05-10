from Bio import Entrez

Entrez.email = "ananyamahesh46@gmail.com"

def fetch_pubmed_abstracts(query, max_results=5):
    try:
        search_handle = Entrez.esearch(db="pubmed", term=query, retmax=max_results)
        search_results = Entrez.read(search_handle)
        id_list = search_results["IdList"]
        abstracts = []

        for pubmed_id in id_list:
            fetch_handle = Entrez.efetch(db="pubmed", id=pubmed_id, rettype="abstract", retmode="text")
            abstract = fetch_handle.read()
            abstracts.append(abstract.strip())
        return abstracts

    except Exception as e:
        print("Error accessing PubMed:", e)
        return []
