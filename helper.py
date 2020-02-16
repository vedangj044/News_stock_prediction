import pandas as pd 

date = input("Enter Date >>> ")
data = pd.read_csv('help.csv')

def avg(date_):
    h = data.loc[date_].High
    l = data.loc[date_].Low
    return (h+l)/2
