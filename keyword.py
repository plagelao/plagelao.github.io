from keybert import KeyBERT

from flair.embeddings import TransformerDocumentEmbeddings

roberta = TransformerDocumentEmbeddings('roberta-base')
kw_model = KeyBERT(model=roberta)

file1 = open("_articles/2023-08-14-consistency-in-version-control.md", "r")

content = file1.read()

kw_model = KeyBERT()

kw_model = KeyBERT(model='all-MiniLM-L6-v2')

keywords = kw_model.extract_keywords(content, keyphrase_ngram_range=(1, 1), stop_words='english', top_n=10)
print(keywords)

keywords = kw_model.extract_keywords(content, keyphrase_ngram_range=(1, 2), stop_words='english')
print(keywords)

keywords = kw_model.extract_keywords(content, keyphrase_ngram_range=(3, 3), stop_words='english', use_maxsum=True, nr_candidates=20, top_n=5)
print(keywords)

keywords = kw_model.extract_keywords(content, keyphrase_ngram_range=(2, 2), stop_words='english', use_mmr=True, diversity=0.7)
print(keywords)

keywords = kw_model.extract_keywords(content, keyphrase_ngram_range=(2, 2), stop_words='english', use_mmr=True, diversity=0.2)
print(keywords)
