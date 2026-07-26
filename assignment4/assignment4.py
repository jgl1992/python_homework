import pandas as pd
data = {
    'Name': ['Alyce', 'Boby', 'Charly'],
    'Age': [25, 30, 35],
    'City': ['NY', 'LA', 'Chi']
}
df = pd.DataFrame('A': [Alyce, Boby, Charly], 'B': [25, 30, 35], 'C':[Ny, LA, Chi] )
print(df)
df_shallow = df.copy(deep=False)
df_shallow.iloc[0, 0] = 50
df.insert(1, 'salary', [70000, 80000, 90000])
df.loc[:, 'Age'] += 1
print("\nUpdated DataFrame:")
print(df)
}
df = pd.DataFrame(task1_data_Frame)
print(df)
df.to_csv('output.csv')
csv_df= pd.read_csv('data.csv')
json_df = pd.read_json('data.json')
combined_df = pd.merge*csv)df, json_df, on= 'user)id', how='left')
first_three.head(n=3)
last_three_rows = df.tail(3)
