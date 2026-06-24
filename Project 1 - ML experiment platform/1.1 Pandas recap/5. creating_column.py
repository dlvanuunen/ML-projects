import pandas as pd

file="drivers.csv"

df=pd.read_csv(file)

df['dob']=pd.to_datetime(df['dob'])
today=pd.Timestamp.today().normalize()



age_years = (today.year-df['dob'].dt.year)
had_birthday =  (today.month < df['dob'].dt.month) |  ((today.month == df['dob'].dt.month) & (today.day < df['dob'].dt.day))

age=age_years-had_birthday

print(age)

df.insert(6, 'age', age.astype("Int64"))

print(df.head(2))
 