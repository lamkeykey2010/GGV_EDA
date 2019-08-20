import os
import pprint as pp
import pandas as pd
import numpy as ny
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

os.getcwd()
path = "/Users/lamkeykey/Desktop/data_analyst"
os.chdir(path)
os.getcwd()

complete = pd.read_csv('df_completed.csv')
order = pd.read_csv('df_order.csv')
region = pd.read_csv('df_region.csv')

print(complete.describe())
print(order.describe())
print(region.describe())

order_group_by = order.groupby(['pickup_location_region']).size()
N=10
print(order_group_by)
df_merge_order = complete.merge(order,left_on='order_request_id',right_on='order_request_id')
print(df_merge_order.describe())
df_merge_order.to_csv('/Users/lamkeykey/Desktop/data_analyst/test.csv',index=True)

df = pd.read_csv('test.csv')
group_driver = df.groupby(['Driver_id']).size()


plt.show()
#plt.show()
#print(day_demand)

#plt.show()




