import pandas as pd
import numpy as np


df=pd.read_excel("data.xlsx")
df.head(5)

print(df.columns)

new_data=df[df["Year"] == 2018]
print(new_data)

new_data['item price'].sum()

item_price = new_data.groupby('Customer ID')["item price"].sum().to_frame()

update_unique=item_price[item_price["item price"]>=584.0]

update_unique.to_csv("new.csv")

value_counts=new_data['Customer ID'].value_counts().to_frame()

print(value_counts)

abc=pd.read_csv("C:\\Users\\rajen\\new.csv")

new_id=list(new_data["Customer ID"])
df=np.ones((445,1),dtype=int)

abc["counts"]=df
print(abc)

print(new_id)

for i in range(445):
#     print(abc["Customer ID"][i])
    value=new_id.count(abc["Customer ID"][i])
    print(value)
    abc["counts"][i]=value

print(abc)

item_price = new_data.groupby('Customer ID')["item price"].sum().to_frame()
print(item_price)

category = new_data.groupby('Customer ID')["Category"].value_counts().to_frame()
category.to_csv("category.csv")

category=pd.read_csv("C:\\Users\\rajen\\category.csv")
print(category)

abc["Category"]=0

for i in range(445):
    value=abc["Customer ID"][i]
    for j in range(1150):
        if value==category["Customer ID"][j]:
            abc["Category"][i]=category["Category"][j]

abc["profit"]=0
print(abc)

for i in range(445):
    if abc["Category"][i]=="college":
        abc["profit"][i]=(abc["item price"][i]*13)/100
        
    elif abc["Category"][i]=="competition ":
        abc["profit"][i]=(abc["item price"][i]*17)/100
        
    elif abc["Category"][i]=="school" or abc["Category"][i]=="School" :
        abc["profit"][i]=(abc["item price"][i]*18)/100
        

abc["Precentage"]=0
print(abc)

for i in range(445):
    if abc["counts"][i]==1:
        abc["Precentage"][i]=10
        
    elif abc["counts"][i]==2:
        abc["Precentage"][i]=11
        
    elif abc["counts"][i]==3:
        abc["Precentage"][i]=12
        
    elif abc["counts"][i]==4:
        abc["Precentage"][i]=13

print(abc)

abc["Give away"]=0

for i in range(445):
    abc["Give away"][i]=(abc["profit"][i]*abc["Precentage"][i])/100

Profit_sum=abc["profit"].sum()
print(Profit_sum)

abc["individual contri"]=0
print(abc)

for i in range(445):
    abc["individual contri"][i]=(abc["profit"][i]/Profit_sum)*100

print(abc)

total_profit=9978.7499999987
total_Give_away=abc["Give away"].sum()
print(total_Give_away)

total_give=total_profit-total_Give_away
print(total_give)

abc["contri"]=0

for i in range(445):
    abc["contri"][i]=(abc["individual contri"][i]*total_give)/100

abc["Total"]=0
for i in range(445):
    abc["Total"][i]=abc["Give away"][i]+abc["contri"][i]