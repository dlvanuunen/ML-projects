# Data source: https://www.daggegevens.knmi.nl/klimatologie/uurgegevens
import pandas as pd
from pathlib import Path

# Load datafile
data_file = Path("./Project 2 - Energy usage forecast/data/weather.csv")
df= pd.read_csv(data_file, skiprows=17)

# Clean column names, renamed to more explicit feature names
df.columns = df.columns.str.strip()
df = df.rename(columns={
    "# STN": "Station number",
"YYYYMMDD": "Date",
"HH": "Time",
"T": "Temperature",
"U": "Relative humidity",
"FH": "Average wind speed",
"FX": "Maximum wind gust",
"SQ": "Sunshine duration",
"Q": "Global radiation",
"N": "Cloud cover",
"RH": "Precipitation amount",
"P": "Air pressure",
   })

# Add DateTime column
df["DateTime"] = (pd.to_datetime(df["Date"], format="%Y%m%d") + pd.to_timedelta(df["Time"], unit="h"))


df = df.sort_values("DateTime")
df = df.set_index("DateTime")

# check
print(df.head(5))
print(df.tail(5))
print(df.describe())


output_file = ("./Project 2 - Energy usage forecast/data/cleaned/weather.csv")
df.to_csv(output_file)






