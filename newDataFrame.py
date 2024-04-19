additional_data = {
    'Name': ['Frank', 'Grace', 'Hannah'],
    'Age': [35, 28, 32],
    'Salary': [75000, 65000, 70000],
    'Department': ['Finance', 'IT', 'HR'],
    'Start_Date': pd.to_datetime(['2019-08-15', '2020-01-10', '2021-03-25']),
    'Experience': [8, 2, 5],
    'Rating': [4.3, 4.1, 4.6]
}
additional_df = pd.DataFrame(additional_data)

concatenated_df = pd.concat([df, additional_df], ignore_index=True)

print(concatenated_df)