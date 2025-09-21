import pandas as pd
import io
from datetime import date

# Data diya gaya hai as a string
data = """
Order ID,Order Date,Category,Product Name,Sales,Quantity,Profit,Region
1,2023-01-05,Electronics,Laptop,1200,1,-200,North
2,2023-01-07,Office Supplies,Pens,15,5,5,North
3,2023-02-10,Furniture,Chair,250,2,50,South
4,2023-02-15,Electronics,Keyboard,75,3,25,North
5,2023-03-20,Furniture,Table,350,1,75,South
6,2023-03-22,Office Supplies,Stapler,10,10,2,East
7,2023-04-01,Electronics,Monitor,400,1,100,West
8,2023-04-15,Furniture,Sofa,800,1,150,East
9,2023-05-02,Office Supplies,Notebooks,20,5,8,West
10,2023-05-10,Electronics,Mouse,50,2,10,North
"""

# String data ko DataFrame mein load karein
df = pd.read_csv(io.StringIO(data))

# DataFrame ko print karke check karein
print(df)

category_sales = df.groupby('Category')['Sales'].sum().reset_index()#reset.index mtlb phr se list ko dataframe mein lana !!!
print(category_sales)
today = date.today()
print(f"Report Date: {today}")
region_profit = df.groupby('Region')['Profit'].sum().reset_index()
most_profitable_region = region_profit.loc[region_profit['Profit'].idxmax()]#loc: location
print("Region-wise Profit:")
print(region_profit)
print("\n------------------------------")
print("Most Profitable Region:")
print(most_profitable_region)