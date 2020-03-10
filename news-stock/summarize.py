from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
import numpy as np
import networkx as nx

class Summarize:
    def __init__(self, file_name, top_n):
        self.file_name = file_name
        self.top_n = top_n

    def read_article(self):
        file = open(self.file_name, "r")
        filedata = file.readlines()
        article = filedata[0].split(". ")
        sentences = []
        
        for sentence in article:
            sentences.append(sentence.replace("[^a-zA-Z]", "").split(" "))
        
        return sentences

    def sentence_similarity(sent1, sent2, stopwords=None):
        if stopwords is None:
            stopwords = []
    
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
    
        for idx1 in range(len(sentences)):
            for idx2 in range(len(sentences)):
                if idx1 == idx2: #ignore if both are same sentences
                    continue 
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