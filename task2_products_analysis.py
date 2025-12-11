import pandas as pd
data=pd.read_csv("datasets/product1.csv")
dd=pd.DataFrame(data)
dd['Total revenue']=dd['Units Sold']*dd['Price Per Unit']
print(dd.to_string(),'\n\n\n')
ss=dd.groupby('Product Name').sum()
print(ss,'\n\n\n')
bestsell=ss['Units Sold'].idxmax()
iprofit=ss['Total revenue'].idxmin()
print(bestsell)
print(iprofit)
