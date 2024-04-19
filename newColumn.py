conditions = [
    (df['Rating'] >= 4.5),
    (df['Rating'] >= 4.0),
    (df['Rating'] >= 3.5),
    (df['Rating'] >= 3.0),
    (df['Rating'] < 3.0)
]
values = ['Excellent', 'Good', 'Satisfactory', 'Needs Improvement', 'Poor']

df['Performance'] = np.select(conditions, values, default='Unknown')

print(df)