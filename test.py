from bs4 import BeautifulSoup
import html5lib 
import requests 
import re
import string

url = 'https://news.google.com/./articles/CBMic2h0dHBzOi8vd3d3Lm5hc2RhcS5jb20vYXJ0aWNsZXMvYXMtdGVzbGEtc3VyZ2VzLWxldHMtZXhwbG9yZS10aGUtZGlmZmVyZW5jZS1iZXR3ZWVuLWNvbXBhbmllcy1hbmQtc3RvY2tzLTIwMjAtMDItMTHSAXdodHRwczovL3d3dy5uYXNkYXEuY29tL2FydGljbGVzL2FzLXRlc2xhLXN1cmdlcy1sZXRzLWV4cGxvcmUtdGhlLWRpZmZlcmVuY2UtYmV0d2Vlbi1jb21wYW5pZXMtYW5kLXN0b2Nrcy0yMDIwLTAyLTExP2FtcA?hl=en-IN&gl=IN&ceid=IN%3Aen'

r = requests.get(url)
r_content = r.content 

soup = BeautifulSoup(r_content, 'html5lib')

news = soup.find_all('p')
news_list = []

for i in range(len(news)):
    if news[i].text.startswith('RELATED') or news[i].text.startswith('Related'):
        pass 
    else:
        text = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+#]|[!*\(\),]|'\
                        '(?:%[0-9a-fA-F][0-9a-fA-F]))+','', str(news[i].text))
        table = str.maketrans(dict.fromkeys(string.punctuation))
        text = text.translat
        news_list.append(text)

final_news = ' '.join(news_list)
print(final_news)

