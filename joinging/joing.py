import pandas as pd


df1=pd.DataFrame({"Int_rate":[2,1,2,3],"IND_GDP":[50,45,45,67]},
                 index=[2001,2002,2003,2004])
df2=pd.DataFrame({"Low_tier_HPI":[12,11,112,31],"Unemployment":[121,451,145,617]},
           index=[2001,2003,2004,2004])


#merge=pd.merge(df1,df2,on="HPI")

joing=df1.join(df2)
print(joing)
