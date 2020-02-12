from classifier import Classify
from news_scraper import scraper

if __name__ == "__main__":
    sc = scraper("Birla stocks").results

    score = 0
    for i in sc:
        value = Classify(i["title"]).classify()
        if value == "Positive":
            score+=1

    print("Score is: {}".format(score/len(sc)))
    print("Total articles {}".format(len(sc)))
