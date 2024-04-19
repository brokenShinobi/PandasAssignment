reshaped_df = df.pivot_table(index='Name', columns='Department', values='Salary', aggfunc='sum')
print(reshaped_df)