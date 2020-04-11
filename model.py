from nltk.corpus import twitter_samples, stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tag import pos_tag
from nltk import NaiveBayesClassifier
import re
import string
import random
import pickle

class Sentiment:
    """
    This class trains the data on 10000 tweets
    """
    def __init__(self):
        self.stop_words = stopwords.words('english')
        self.positive_cleaned_tokens_list = []
        self.negative_cleaned_tokens_list = []
        self.positive_tweets_tokens = twitter_samples.tokenized('positive_tweets.json')
        self.negative_tweets_tokens = twitter_samples.tokenized('negative_tweets.json')


    def remove_noise(self, token_):
        cleaned_tokens = []

        for token, tag in pos_tag(token_):
            # Here regex removes the unwanted hyperlinks and username preceded by @
            token = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+#]|[!*\(\),]|'\
                       '(?:%[0-9a-fA-F][0-9a-fA-F]))+','', token)
            token = re.sub("(@[A-Za-z0-9_]+)","", token)

            if tag.startswith('NN'):
                pos = 'n'
            elif tag.startswith('VB'):
                pos = 'v'
            else:
                pos = 'a'

            lemmatizer = WordNetLemmatizer()
            token = lemmatizer.lemmatize(token, pos)

            if len(token)>0 and token not in string.punctuation and token.lower() not in self.stop_words:
                cleaned_tokens.append(token.lower())

        return cleaned_tokens


    def get_tweet_for_model(self, cleaned_tokens_list):
        for tweet_tokens in cleaned_tokens_list:
            yield dict([token, True] for token in tweet_tokens)


    def preprocess_data(self):

        for tokens in self.positive_tweets_tokens:
            self.positive_cleaned_tokens_list.append(self.remove_noise(tokens))

        for tokens in self.negative_tweets_tokens:
            self.negative_cleaned_tokens_list.append(self.remove_noise(tokens))

        positive_tokens_for_model = self.get_tweet_for_model(self.positive_cleaned_tokens_list)
        negative_tokens_for_model = self.get_tweet_for_model(self.negative_cleaned_tokens_list)

        positive_dataset = [(tweet_dict, "Positive") for tweet_dict in positive_tokens_for_model]
        negative_dataset = [(tweet_dict, "Negative") for tweet_dict in negative_tokens_for_model]

        dataset = positive_dataset + negative_dataset

        random.shuffle(dataset)

        # Splitting data [70:30 ratio]
        train_data = dataset[:7000]
        test_data = dataset[7000:]

        return train_data, test_data


    def train_data(self):
        train_set = self.preprocess_data()[0]
        classifier = NaiveBayesClassifier.train(train_set)
        f = open('my_classifier.pickle', 'wb')
        pickle.dump(classifier, f)
        return classifier


Sentiment().train_data()
