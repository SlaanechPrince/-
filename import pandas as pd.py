import pandas as pd
data = pd.read_csv("nbaNew.csv")
data.head(3)

for i,j in  data.iterrows():
    print(i,j)
    print()

