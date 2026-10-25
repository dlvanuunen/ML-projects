import pandas as pd

file="drivers.csv"

df=pd.read_csv(file)

# sort by Nan counts manually:
nan_count_column= []

for col in df.columns:
    print('column: ',col," example: ", df[col][0])
    # print(df[col].isna())
    nan_count= int(df[col].isna().sum())
    print("nan: ", nan_count)
    nan_count_column.append((col, nan_count))

print("Missing data per column")
nan_count_column.sort(key=lambda item: item[1], reverse=True)
print(nan_count_column)


# Pandas faster function
print(df.isna().sum().sort_values(ascending=False))

