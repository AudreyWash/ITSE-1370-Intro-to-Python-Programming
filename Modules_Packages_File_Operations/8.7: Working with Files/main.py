import pandas as pd


try:
    df = pd.read_csv('employees.csv')
except FileNotFoundError:
    print("Error: The file 'employees.csv' was not found.")
    exit(1)


if 'hours_worked' in df.columns:
    df['pay_rate'] = df['hours_worked'] * 15  
else:
    print("Error: 'hours_worked' column not found in the CSV file.")
    exit(1)


df.drop(columns=['hours_worked'], inplace=True)


df.to_csv('wages.csv', index=False)  


print("Wages calculated and saved to 'wages.csv'.")