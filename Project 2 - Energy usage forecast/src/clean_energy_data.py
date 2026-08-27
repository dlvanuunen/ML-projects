import pandas as pd
from pathlib import Path
import plotly.graph_objects as go
import plotly.io as pio
pio.renderers.default = "browser"

# Load combined dataset
data_file = Path("./Project 2 - Energy usage forecast/data/combined_hourly_load2.csv")
print(data_file)

df = pd.read_csv(data_file, parse_dates=['DateUTC'])


#Filter for Netherlands values only
df_NL= df[df['CountryCode']=='NL']

#set index to timestamp and sort
df_NL = df_NL.sort_values("DateUTC")
df_NL = df_NL.set_index('DateUTC')







#Check / explore dataset
print("head:", df_NL.head(5))
print("tail:", df.tail(5))
# print(df_NL.dtypes)
print(df_NL.describe())
# value_mean = df_NL["Value"].mean()
# print(value_mean)


# #prepare plot
# x = df_NL.index
# y = df_NL['Value']

# fig = go.Figure()
# fig.add_trace(
#     go.Scatter(
#         x=x,
#         y=y,
#         mode='lines'
#     )
# )
# fig.show()


# #resampling for daily median values of the load
# df_NL_daily = df_NL['Value'].resample('D').mean()
# x = df_NL_daily.index
# y = df_NL_daily

# fig = go.Figure()
# fig.add_trace(
#     go.Scatter(
#         x=x,
#         y=y,
#         mode='lines'
#     )
# )
# fig.show()



# #resampling for monthly median values of the load
# df_NL_monthly = df_NL['Value'].resample('ME').median()
# x = df_NL_monthly.index
# y = df_NL_monthly

# fig = go.Figure()
# fig.add_trace(
#     go.Scatter(
#         x=x,
#         y=y,
#         mode='lines'
#     )
# )

# fig.show()