df.loc[2, 'Salary'] = np.nan

mean_salary = df['Salary'].mean()

df['Salary'] = df['Salary'].fillna(mean_salary)

print(df)