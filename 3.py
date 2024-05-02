import pandas as pd
data = pd.read_csv("nbaNew.csv")
data.head(3)
for key,value in data.items():
    print(key,value)
    print()