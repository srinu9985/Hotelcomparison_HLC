import pandas as pd 
import numpy as np 
df=pd.read_excel("files/report.xlsx",header=None) 

# drop the empty rows and columns
df.dropna(how='all',axis="rows",inplace=True)
df.dropna(how='all',axis="columns",inplace=True)

# reset indexes
df.reset_index(inplace=True,drop=True)   
df.columns=np.arange(0,len(df.columns))

# combine columns using fillna method
df[2]=df[2].fillna(df[3])
df[4]=df[4].fillna(df[5])
df[6]=df[6].fillna(df[7])
df.drop(columns=[3,5,7],inplace=True)
df.columns=np.arange(0,len(df.columns))
df.drop(columns=6,inplace=True)

# combine rows
mrow= df.iloc[2].combine_first(df.iloc[3])
df.iloc[2] = mrow
df = df.drop(3)

df.to_csv("output/HLC_task1.csv")