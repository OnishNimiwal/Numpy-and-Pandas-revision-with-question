import pandas as pd
import numpy as np

#1. Load a CSV file into a Pandas DataFrame
df=pd.read_csv("data.csv")
print(df)

#2. Create a DataFrame from a NumPy array with custom column names.
data=np.array([["Onish",22],["Ojaswi",22],["Prshotam",20]])
df=pd.DataFrame(data,columns=["Name","Age"])
print(df)

#3. Select rows from a DataFrame based on multiple conditions.
data = {'Name': ['Teodosija', 'Sutton', 'Taneli', 'Ravshan', 'Ross'],
        'Age': [26, 32, 25, 31, 28],
        'Salary': [50000, 60000, 45000, 70000, 55000]}
df=pd.DataFrame(data)
df1=df.query("Age >= 26 and 40000 <= Salary <=50000")
print(df1)

#4. Select the first and last 3 rows of a Pandas DataFrame.
first_row=pd.concat([df.head(3)])
last_3rows=pd.concat([df.tail(3)])
print(first_row)
print(last_3rows)

#5. Filter rows based on a condition in a specific column in a Pandas DataFrame.
specific_age=df[df["Age"]>26]
print(specific_age)

#6. Create a new column in a Pandas DataFrame based on the result of a NumPy operation.
df["Result"]=df["Age"].apply(lambda x:"Qualified" if x >=31 else "Not Qualified")
print(df)

#7. Merge two Pandas DataFrames based on a common column.

df1 = pd.DataFrame({
    "EmpID": [1, 2, 3],
    "Name": ["Amit", "Neha", "Ravi"]
})

df2 = pd.DataFrame({
    "EmpID": [2, 3, 4],
    "Department": ["HR", "IT", "Finance"]
})
merged_df=pd.merge(df1,df2,on="EmpID")
print(merged_df)

#8. Extract rows from a Pandas DataFrame where a specific column's values are in a given NumPy array.
data = {'Name': ['Teodosija', 'Sutton', 'Taneli', 'Ravshan', 'Ross'],
        'Age': [26, 32, 25, 31, 28],
        'Salary': [50000, 60000, 45000, 70000, 55000]}
df=pd.DataFrame(data)
arr=np.array([26,32])
df=df[~df["Age"].isin(arr)]
print(df)

#9. Perform element-wise addition of a NumPy array and a Pandas DataFrame column.
data = {'Name': ['Teodosija', 'Sutton', 'Taneli', 'Ravshan', 'Ross'],
        'Age': [26, 32, 25, 31, 28],
        'Salary': [50000, 60000, 45000, 70000, 55000]}
df=pd.DataFrame(data)
arr=np.array([1000,1100,2000,2200,3000])
df["updated_salary"]=np.add(df["Salary"],arr)
print(df)

#10. Apply a NumPy function to a Pandas DataFrame column.
mean=np.mean(df["Age"])
print(mean)

#11. Calculate the correlation matrix for a Pandas DataFrame.
data = {'Age': [25, 30, 22, 35, 28],
        'Salary': [50000, 60000, 45000, 70000, 55000],
        'Experience': [2, 5, 1, 8, 4]}

df = pd.DataFrame(data)
result=df.corr()
print(result)

#12. Calculate the cumulative sum of a NumPy array and store the results in a new Pandas DataFrame column.
arr=np.array([22,22,33,33,44,44,55])
df["CumSum"]=pd.DataFrame(np.cumsum(arr))
print(df)

#13. Group a Pandas DataFrame by a column and calculate the mean of another column.
data = {
    "name": ["Amit", "Rohit", "Neha", "Priya", "Karan", "Sneha"],
    "salary": [50000, 60000, 55000, 65000, 52000, 58000],
    "age": [25, 28, 26, 30, 24, 27],
    "position": ["Developer", "Developer", "Designer", "Developer", "Designer", "Designer"]
}
df=pd.DataFrame(data)
print(df)
df["Avg_Salary_Position"]=df.groupby("position")["salary"].transform("mean")
print(df)

#14. Reshape a Pandas DataFrame using the pivot_table function.
data = {
'Name': ['Alice', 'Bob', 'Charlie'],
'Math': [85, 78, 92],
'Science': [90, 82, 89],
'English': [88, 85, 94]
}
df=pd.DataFrame(data)
print(df)
df=df.melt(
        id_vars="Name",
        value_vars=["Math","Science","English"],
        var_name="Subject",
        value_name="Scores",
)
print(df)
df=df.pivot(index="Name", columns="Subject", values="Scores").reset_index()
print(df)

#15. Replace missing values in a Pandas DataFrame with the mean of the column.
data = {
    "Name": ["Amit", "Rohit", "Neha", "Priya", "Karan"],
    "Age": [25, np.nan, 26, np.nan, 24],
    "Salary": [50000, 60000, np.nan, 65000, np.nan]
}

df = pd.DataFrame(data)
print(df)
df["Age"]=df["Age"].fillna(df["Age"].mean())
df["Salary"]=df["Salary"].fillna(df["Salary"].mean())
print(df)

#16. Normalize a numerical column in a Pandas DataFrame.
data = {
    "Name": ["Amit", "Rohit", "Neha", "Priya", "Karan"],
    "Age": [22, 25, 24, 27, 23],
    "Salary": [30000, 50000, 45000, 60000, 40000]
}
df=pd.DataFrame(data)
print(df)
mean_age=df["Age"].mean()
std_age=df["Age"].std()
df["Age"]=(df["Age"]-mean_age)/std_age


mean_salary=df["Salary"].mean()
std_salary=df["Salary"].std()
df["Salary"]=(df["Salary"]-mean_salary)/std_salary
print(df)

#17. Remove duplicate rows from a Pandas DataFrame.
data = {
    "Name": ["Amit", "Rohit", "Amit", "Neha", "Rohit"],
    "Age": [25, 28, 25, 26, 28],
    "Salary": [50000, 60000, 50000, 55000, 60000]
}

df = pd.DataFrame(data)
print(df)
df=df.drop_duplicates(subset=["Name", "Age"])
print(df)

#18. Calculate the dot product of two NumPy arrays
array1=np.array([1,2,3,4,5,6])
array2=np.array([6,5,4,3,2,1])
result=np.dot(array1,array2)
print(result)

#19. Find the index of the maximum and minimum value in a NumPy array.
arr=np.array([1,2,3,4,5,6])
ind=np.argmin(arr)
ind1=np.argmax(arr)
print(f"The index of mini is {ind} and that of maximum is {ind1}")

#20. Reshape a 1D NumPy array into a 2D array.
arr=np.array([2,2,1,44,23,61,13,21])
arr1=arr.reshape(4,2)
print(arr1)

#21. Slice and extract a portion of a NumPy array.
arr3=arr1[0:2,:]
print(arr3)

#22. Concatenate two NumPy arrays vertically.
array1 = np.array([[1, 2, 3],
                   [4, 5, 6]])

array2 = np.array([[7, 8, 9],
                   [10, 11, 12]])

result_array = np.vstack((array1, array2))
#or
result_array2=np.concatenate((array1,array2),axis=0)
print(result_array==result_array2)

#23. matrix multiplication using numpy
arr1=np.array([[2,3,4,4],[1,2,3,4]])
arr2=np.array([[1,2],[3,4],[5,6],[7,8]])
muli=np.dot(arr1,arr2)
print(muli)

#24. Generate the random integer np array and find number of unique elements in it
arr=np.random.randint(low=1,high=10,size=15,dtype="int64")
print(arr)
count=np.unique(arr).size
print(count)
arr=set(arr)
print(len(arr))

#25. Sort a Pandas DataFrame by values in a specific column.

data = {
    "Name": ["Amit", "Rohit", "Amit", "Neha", "Rohit"],
    "Age": [25, 28, 25, 26, 28],
    "Salary": [50000, 60000, 50000, 55000, 60000]
}

df = pd.DataFrame(data)
print(df)
df.sort_values("Age",inplace=True)
df.reset_index(drop=True,inplace=True)
print(df)

#26. rename columns
df.rename(columns={"Age":"AGE"},inplace=True)
print(df)

#27. Create New df using the transpose
df2=df.transpose()
print(df2)

#28. Use merge and then merge two df using two columns
data1 = {'ID': [1, 2, 3, 4],
         'Name': ['Imen', 'Karthika', 'Cosimo', 'Cathrine'],
         'Department': ['HR', 'IT', 'Finance', 'IT']}

data2 = {'ID': [1, 2, 3, 5],
         'Salary': [50000, 60000, 45000, 70000],
         'Department': ['HR', 'IT', 'Finance', 'Marketing']}
df1=pd.DataFrame(data1)
df2=pd.DataFrame(data2)

df3=pd.merge(df1,df2,on=["ID","Department"],how="inner")
print(df3)

#29. aggregate the data on multiple columns
data = {'Department': ['HR', 'IT', 'Finance', 'IT', 'HR', 'Finance'],
        'Salary': [50000, 60000, 45000, 70000, 55000, 60000],
        'Experience': [2, 5, 1, 7, 3, 4]}
df=pd.DataFrame(data)
print(df)
new_df=df.groupby("Department").agg({
    "Salary":["mean","sum"],
    "Experience":"max"
}).reset_index()
print(new_df)

#30. Extract the date and time components from a DateTime column.
data = {'DateTime': ['2012-01-01 08:30:00', '2012-01-02 12:45:00', '2012-01-03 18:15:00']}
df=pd.DataFrame(data)
df["DateTime"]=pd.to_datetime(df["DateTime"])
df["Date"]=df["DateTime"].dt.date
df["Time"]=df["DateTime"].dt.time
print(df)

#31. Resample time-series data in a DataFrame.
#resampling doesnot understand

#32. Perform Rolling function
data={
    "Value":[10, 15, 20, 25, 30, 35, 40, 45, 50]
}
df=pd.DataFrame(data)
df["Rolling_Mean"]=df["Value"].rolling(window=3).mean()
print(df)

#33.Perform Cross Tabulation
data = {'Category': ['A', 'B', 'A', 'B', 'C', 'A', 'C', 'C', 'B', 'A'],
        'Value': [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]}
df=pd.DataFrame(data)
print(df)
cross_tab=pd.crosstab(df["Category"],df["Value"])
print(cross_tab)