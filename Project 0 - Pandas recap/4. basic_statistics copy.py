import pandas as pd

file="drivers.csv"

df=pd.read_csv(file)


for col in df.columns:
    series= df[col]
    datatype= series.dtypes


    print('column: ',col)
    print('example: ', series[0])    
    print('data type: ', datatype )

    if datatype=='float64':
        print('mean: ', series.mean)
        print('median: ', series.median)
        print('stdev: ', series.std)
    
    print('___')
    


