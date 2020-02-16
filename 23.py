import pandas as pd 
from classifier import Classify

data = pd.read_csv('help.csv')

def avg(date_):
    h = data.loc[date_].High
    l = data.loc[date_].Low
    return (h+l)/2

l = open("india.csv")

g = []

month = {"01": "Janurary",
"02": "Feburary",
"03": "March",
"04": "April",
"05": "May",
"06": "June",
"07": "July",
"08": "August",
"09": "September",
"10": "October",
"11": "November",
"12": "December"}

avg_arr = []

count = 0
for i in l.readlines():
    if "business.india-business" in str(i):
        if int(i.split(",")[0][0:4]) >= 2010:
            date = str(int(i.split(",")[0][6:8]))+"-"+month[i.split(",")[0][4:6]]+"-"+i.split(",")[0][0:4]
            try:
                avg_val = avg(date)
                score = Classify(i.split(",")[1].replace(',', '')).classify()
                avg_arr.append((score, avg_val))
                count+=1
                print((count/4300)*100)
                break
            except:
                pass

f = open('fuck.txt', 'w')
f.write(str(avg_arr))
f.close()


