import pandas as pd
import numpy as np
import sqlite3

#from pandas list
data=[
    ["Onish",22],
    ["Ojaswi",22],
    ["Prshotam",20]
]
df=pd.DataFrame(data,columns=["Name","Age"])
print(df)

#from dictionary of lists
data={
    "Name":["Onish","Ojaswi","Prshotam"],
    "Age":[22,22,20]
}
df=pd.DataFrame(data)
print(df)

#from numpy array
data=np.array([["Onish",22],["Ojaswi",22],["Prshotam",20]])
df=pd.DataFrame(data,columns=["Name","Age"])
print(df)

#from.csv
df=pd.read_csv("data.csv")
print(df)

#from excel
df=pd.read_excel("data.xlsx")
print(df)

#from json
df=pd.read_json("data.json")
print(df)

#from sqlite3 database
conn = sqlite3.connect("mydb.sqlite")
df = pd.read_sql("SELECT * FROM users", conn)
print(df)

#from url
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv(url)
print(df)


