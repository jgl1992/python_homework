import pandas as pd

# Correct initial data
data = {
    'Name': ['Alyce', 'Boby', 'Charly'],
    'Age': [25, 30, 35],
    'City': ['NY', 'LA', 'Chi']
}

df = pd.DataFrame(data)
print(df)

# Shallow copy
df_shallow = df.copy(deep=False)
df_shallow.iloc[0, 0] = "50"   # modifies df too

# Proper deep copy for salary column
df_copy = df.copy()
df_copy['salary'] = [70000, 80000, 90000]

# Add one year to Age
df.loc[:, 'Age'] += 1
df_copy['age'] = df_copy['age'] + 1
print("\nUpdated DataFrame:")
print(df)

# Save to CSV
df.to_csv('output.csv', index=False)

# Load CSV and JSON
csv_df = pd.read_csv('data.csv')
json_df = pd.read_json('data.json')

# Correct merge syntax
combined_df = pd.merge(csv_df, json_df, on='user_id', how='left')

# First 3 rows
first_three = df.head(3)

# Last 3 rows
last_three_rows = df.tail(3)

# Shape of df
print(df.shape)
json_employees = pd.read_json('additional_employees.json')
import pandas as pd
import numpy as np

# 1. Load dirty data
dirty_data = pd.read_csv("dirty_data.csv")
print("DIRTY DATA:")
print(dirty_data)

# 2. Create a clean copy
clean_data = dirty_data.copy()
print("\nCLEAN COPY CREATED:")
print(clean_data)

# 3. Remove duplicate rows
clean_data = clean_data.drop_duplicates()
print("\nAFTER REMOVING DUPLICATES:")
print(clean_data)

# 4. Convert Age to numeric and handle missing values
clean_data["Age"] = pd.to_numeric(clean_data["Age"], errors="coerce")
print("\nAGE AS NUMERIC:")
print(clean_data)

# 5. Convert Salary to numeric and replace placeholders
clean_data["Salary"] = clean_data["Salary"].replace(["unknown", "n/a"], np.nan)
clean_data["Salary"] = pd.to_numeric(clean_data["Salary"], errors="coerce")
print("\nSALARY CLEANED:")
print(clean_data)

# 6. Fill missing numeric values
clean_data["Age"] = clean_data["Age"].fillna(clean_data["Age"].mean())
clean_data["Salary"] = clean_data["Salary"].fillna(clean_data["Salary"].median())
print("\nAFTER FILLING MISSING VALUES:")
print(clean_data)

# 7. Convert Hire Date to datetime
clean_data["Hire Date"] = pd.to_datetime(clean_data["Hire Date"], errors="coerce")
print("\nHIRE DATE AS DATETIME:")
print(clean_data)

# 8. Strip whitespace + uppercase Name and Department
clean_data["Name"] = clean_data["Name"].str.strip().str.upper()
clean_data["Department"] = clean_data["Department"].str.strip().str.upper()
print("\nFINAL CLEANED DATA:")
print(clean_data)
