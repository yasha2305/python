import pandas as pd

data = {
    'EmpID': [101, 102, 103, 104, 105],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Department': ['HR', 'IT', 'IT', 'Finance', 'HR'],
    'Salary': [50000, 75000, 80000, 65000, 52000],
    'Age': [28, 34, 29, 41, 25]
}

df = pd.DataFrame(data)

df.drop('Age', axis=1, inplace=True)

print(df)