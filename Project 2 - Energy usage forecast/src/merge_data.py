import pandas as pd
from pathlib import Path

files = Path("Project 2 - Energy usage forecast/data").glob("*.csv")

#Check seperation symbol for files
# for file in files:
#     with open(file, "r", encoding="utf-8-sig") as f:
#         print("\n", file)
#         print(f.readline())

#load all dataframes with correct seperation symbol and time format
dataframes = []
print('before')
print(dataframes)

for i, file in enumerate(files):
    print("start file loading")

    if i in [1,2]:
        sep = ";"
        formatt = "%d/%m/%Y %H:%M"
    else:
        sep = "\t"
        formatt = "%d-%m-%Y %H:%M"

    df = pd.read_csv(
        file,
        sep=sep,
        engine="python"
    )
    df['DateUTC']= pd.to_datetime(df['DateUTC'], format=formatt, dayfirst=True)
    dataframes.append(df)

for frame in dataframes:

    print(frame.head(2))
# Combine all dataframes
combined = pd.concat(dataframes, ignore_index=True)
combined.to_csv("combined_hourly_load2.csv", index=False)
