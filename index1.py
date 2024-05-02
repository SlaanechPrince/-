# importing pandas
import pandas as pd 
dict = {'name' : [ "aparna","pankaj","sudhir","Geeku"],
        'degree' : ["MBA","BCA","M.Tech","MBA"],
        'score' : [90,40,80,98]}
df = pd.DataFrame(dict)
for i,j in df.iterrows():
    print(i,j)
    print()