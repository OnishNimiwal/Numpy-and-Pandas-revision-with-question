import pandas as pd

#Series 1-D labeled array
s=pd.Series([10,20,30,40],index=["a","b","c","d"])
print("Series:",s)
#Data Frame 2-D array with labels row and column wise both
data={
    "name":["Alice","Bob","Onish"],
    "age":[20,30,21],
    "position":["HR","Product Manger","Software Engineer"]
}

df=pd.DataFrame(data)
print(df)
#Each column of dataframe is series

#row wise labels
print(df.index)
df.index=["a","b","c"]
print(df.index)

#columns wise labels
print(df.columns)
df.columns=["NAME","AGE","POSITION"]
print(df.columns)
