import gensim.downloader as api

info_datasets = api.info()
# print(info_datasets)
dataset_info = api.info("text8")
dataset = api.load("text8")
word2vec_model = api.load('glove-wiki-gigaword-50')

# Example usage of the word2vec model
word = "programmer"
similar_words = word2vec_model.most_similar(word)

print(f"Words similar to '{word}':")
for similar_word, similarity in similar_words:
    print(f"{similar_word}: {similarity:.4f}")