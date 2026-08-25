import pandas as pd
from pathlib import Path

files = Path("Project 2 - Energy usage forecast/data").glob("*.csv")





for file in files:
    with open(file, "r", encoding="utf-8-sig") as f:
        print("\n", file)
        print(f.readline())


# dataframes = []
# for i, file in enumerate(files):

#     if i in [1,2]:
#         sep = ";"
#     else:
#         sep = "\t"

#     df = pd.read_csv(
#         file,
#         sep=sep,
#         engine="python"
#     )
#     dataframes.append(df)
 
# combined = pd.concat(dataframes, ignore_index=True)


# combined.to_csv("combined_hourly_load.csv", index=False)