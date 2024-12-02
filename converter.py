import pandas as pd

# Replace 'your_excel_file.xlsx' with the path to your Excel file
df = pd.read_excel("C:\\Users\\A\\Desktop\\realestate_21_22_23_updated.xlsx")

print(df.dtypes)  

from sqlalchemy import create_engine

# Replace the placeholders with your actual database credentials
engine = create_engine('postgresql+pg8000://postgres:123456@localhost:5432/postgres')

# Example:
# engine = create_engine('postgresql+psycopg2://postgres:mysecretpassword@localhost:5432/mydatabase')

# Replace 'your_table_name' with the desired table name in PostgreSQL
df.to_sql('your_table_name', engine, if_exists='replace', index=False)
