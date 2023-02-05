import pandas as pd

# Load csv file into dataframe
df = pd.read_csv("Resources/employees.csv")

# Convert date columns to ISO format
df['birth_date'] = pd.to_datetime(df['birth_date'], format='%m/%d/%Y').dt.strftime('%Y-%m-%d')
df['hire_date'] = pd.to_datetime(df['hire_date'], format='%m/%d/%Y').dt.strftime('%Y-%m-%d')

# Save the dataframe as a new csv file
df.to_csv("Resources/employees.csv", index=False)
