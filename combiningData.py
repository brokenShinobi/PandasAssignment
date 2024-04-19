bonus_data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Bonus': [5000, 6000, 7000, 8000, 9000]
}
bonus_df = pd.DataFrame(bonus_data)

merged_df = pd.merge(df, bonus_df, on='Name', how='left')

print(merged_df)