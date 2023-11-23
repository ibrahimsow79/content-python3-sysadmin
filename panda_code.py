#!/usr/bin/env python3.8

import pandas as pd

data = {'Name' :['John', 'Emily', 'Kate', 'Mike'],
        'Age':[25,30,28,35],  
         'City':['New York','Paris', 'London', 'Sydney']}
df = pd.DataFrame(data)
print(df)

df_filtered = df[df['Age'] > 28 ]
print(df_filtered) 