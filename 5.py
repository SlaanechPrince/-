import pandas as pd
data= pd.read_csv ("nbaNew.csv")
data.head(3)
for i in data.itertuples():
    print(i)
    print()