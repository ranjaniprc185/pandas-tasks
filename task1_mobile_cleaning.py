import pandas as pd
data=pd.read_csv("datasets/Smartphones.csv")
df=pd.DataFrame(data)
df.replace(['n/a','NA'],pd.NA,inplace=True)
df.fillna("unknown",inplace=True)
print(df)
mobiles=df[['brand_name','model','price','avg_rating','ram_capacity']].copy()
print(mobiles)
mobiles=mobiles.iloc[:-200,:]
print(mobiles)
print(len(mobiles))
mobiles=mobiles[mobiles['ram_capacity']!="unknown"]
print(mobiles)
print(len(mobiles))
