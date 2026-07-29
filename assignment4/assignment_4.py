*/justina's Task 1/*
import pandas as pd
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}
df = pd.DataFrame(data)
print(df)
df_with_salary = df.copy()
df_with_salary["Salary"] = [70000, 80000, 90000]
print(df_with_salary)
df_older = df_with_salary.copy()
df_older["Age"] = df_older["Age"] + 1
print(df_older)
df.to_csv("employees.csv", index=False)
*/justina's Task 2/*
pd.read_csv("employees.csv") 
pd.read_json("additional_employees.json")
df1 = pd.DataFrame({"Name": ["Alice",], "Age": [25]}) 
df2 = pd.DatFrame({"Name": ["Bob"], "Age": [30]})
combined = pd.concat([df1, df2],ignore_index = True')
print(combined)
*/ justina's task 3/*
first_three=df.head(3) 
last_two=df.tail(2)
more_employees=df.shape
df.shape

