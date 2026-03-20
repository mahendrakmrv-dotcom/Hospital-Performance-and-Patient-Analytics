import pandas as pd
from sqlalchemy import create_engine

a=pd.read_csv('Final_Cleaned_Hospital_Data.csv')

df = pd.DataFrame(a)


username="root",
password="root",
host="localhost",
port="3306",
database="hospital"

engine=create_engine(f"mysql+pymysql://root:root@localhost:3306/hospital")
table_name="reports"
df.to_sql(table_name,engine,if_exists='replace',index=False)