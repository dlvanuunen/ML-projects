import pandas as pd

file="drivers.csv"

df=pd.read_csv(file)

df['dob']=pd.to_datetime(df['dob'])
today=pd.Timestamp.today().normalize()

# Calculate age based on current years month and date
age_years = (today.year-df['dob'].dt.year)
had_birthday =  (today.month < df['dob'].dt.month) |  ((today.month == df['dob'].dt.month) & (today.day < df['dob'].dt.day))
age=age_years-had_birthday

# Add column next to date of birth
# Note: No information is present on date of death, thus age is not a reiable.
df.insert(6, 'age', age.astype("Int64"))


result = df[(df['age']>100) & (df['nationality']=="British")] 
print(result)


# Groupby