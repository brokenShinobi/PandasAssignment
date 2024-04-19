import pandas as pd 
import numpy as np
 # Creating a dummy dataset 
data = { 
  'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'], 
  'Age': [25, 30, 35, 40, 45], 
  'Salary': [50000, 60000, 70000, 80000, 90000], 
  'Department': ['HR', 'IT', 'Finance', 'HR', 'IT'], 
  'Start_Date': pd.to_datetime(['2020-01-01', '2019-03-15', '2021-05-20', '2018-09-10', '2022-02-28']), 
  'Experience': [5, 10, 3, 15, 2], 
  'Rating': [4.2, 3.8, 4.5, 4.0, 4.7] 
  } 
df = pd.DataFrame(data) 
df