import pandas as pd
a=5
print(a)
file="circuits.csv"

df=pd.read_csv(file)

print("Shape: ",df.shape)
print("Column names: ",df.columns)
# print("5 rows: ", df.head(5))


selected_columns = ["country",'lat', 'long']


for col in selected_columns:
    subset=df[col]
    col_name = subset.name
    
    try:
        col_summary=subset.describe()
    except:
        col_summary="no statistics avaiable"
    
    col_amount= subset.count()

    print(f"name: {col_name} \n summary: {col_summary} \n amount: {col_amount}    ")



    
