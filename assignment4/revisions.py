import pandas as pd
task1_data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}
task1_data_frame = pd.DataFrame(task1_data)
print("Task 1 - Original DataFrame:")
print(task1_data_frame)
print()
task1_with_salary = task1_data_frame.copy()
task1_with_salary["Salary"] = [70000, 80000, 90000]
print("Task 1 - DataFrame with Salary:")
print(taask1_with_salary)
print()
task1_older = task1_with_salary.copy()
task1_older["Age"] = task1_older["Age"] + 1
print("Task 1 - Employees One Year Older:")
print(task1_older)
print()
task1_older.to_csv("employees.csv", index=False)
print("Task 1 - employees.csv created.")
print()
task1_data_frame = pd.DataFrame(task1_data)
print("Task 1 - Original DataFrame:")
print(task1_data_frame)
print()
json_df = pd.read_json("additional_employees.json")  
print("JSON DataFrame:")
print(json_df.head())
print()
csv_df = pd.read_csv("employees.csv")
combined_df = pd.merge(csv_df, json_df, on="user_id", how="left")
print("Combined DataFrame:")
print(combined_df)
