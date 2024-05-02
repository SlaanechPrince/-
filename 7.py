import pandas as pd
data=pd.read_csv("nbaNew.csv")
col= data.head(3)
col
clmn=list(col)
for i in clmn:
    print(col[i][2])
    