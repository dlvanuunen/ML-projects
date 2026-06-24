import pandas as pd
a=5
print(a)
file="circuits.csv"

df=pd.read_csv(file)

print("Shape: ",df.shape)
print("Column names: ",df.columns)
print("5 rows: ", df.head(5))