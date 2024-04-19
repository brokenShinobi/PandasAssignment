grouped_stats = df.groupby('Department').agg({'Salary': 'mean', 'Experience': 'mean'})

# Rename the columns for clarity
grouped_stats = grouped_stats.rename(columns={'Salary': 'Mean_Salary', 'Experience': 'Mean_Experience'})

# Display the group-wise summary statistics
print(grouped_stats)