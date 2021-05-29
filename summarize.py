from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
import numpy as np
import networkx as nx

class Summarize:

    def __init__(self, text, top_n):
        """Get the summary of the text of news scraped."""
        self.text = text
        self.top_n = top_n

    def read_article(self):

        article = self.text.split(". ")
        sentences = []

        for sentence in article:
            sentences.append(sentence.replace("[^a-zA-Z]", "").split(" "))

        return sentences

    @staticmethod
    def sentence_similarity(sent1, sent2, stopwords):

        sent1 = [w.lower() for w in sent1]
        sent2 = [w.lower() for w in sent2]

        all_words = list(set(sent1 + sent2))

        vector1 = [0] * len(all_words)
        vector2 = [0] * len(all_words)

        # build the vector for the first sentence
        for w in sent1:
            if w in stopwords:
                continue
            vector1[all_words.index(w)] += 1

        # build the vector for the second sentence
        for w in sent2:
            if w in stopwords:
                continue
            vector2[all_words.index(w)] += 1

        return 1 - cosine_distance(vector1, vector2)

    def build_similarity_matrix(self, sentences, stop_words):
        # Create an empty similarity matrix
        similarity_matrix = np.zeros((len(sentences), len(sentences)))

        for idx1, _ in enumerate(sentences):
            for idx2, _ in enumerate(sentences):
                if idx1 == idx2: #ignore if both are same sentences
                    continue
                # print(sentences[idx1], sentences[idx2], stop_words)
                similarity_matrix[idx1][idx2] = self.sentence_similarity(sentences[idx1], sentences[idx2], stop_words)

        return similarity_matrix


    def generate_summary(self):
        stop_words = stopwords.words('english')
        summarize_text = []

        sentences = self.read_article()

        sentence_similarity_martix = self.build_similarity_matrix(sentences, stop_words)

        sentence_similarity_graph = nx.from_numpy_array(sentence_similarity_martix)
        scores = nx.pagerank(sentence_similarity_graph)

        ranked_sentence = sorted(((scores[i],s) for i,s in enumerate(sentences)), reverse=True)

        for i in range(self.top_n):
            summarize_text.append(" ".join(ranked_sentence[i][1]))

        summary = "".join(summarize_text)
        return summary
