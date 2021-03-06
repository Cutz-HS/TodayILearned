import numpy as np
import pandas as pd


'''
stock
'''
data=[[828.659973,833.450012,828.349976,1247700,831.659973],
      [823.02002,828.070007,821.655029,1597800,828.070007],
      [819.929993,824.400024,818.97998,1281700,824.159973],
      [819.359985,823,818.469971,1304000,818.97998],
      [819,823,816,1053600,820.450012],
      [816,820.958984,815.48999,1198100,819.23999],
      [811.700012,815.25,809.780029,1129100,813.669983],
      [809.51001,810.659973,804.539978,989700,809.559998]]

data=np.array(data)
#print(data.shape)
#print(data)
#print("="*50)
data=np.transpose(data)
#print(data.shape)
#print(data)

x=data[:-1].transpose

'''
diabetes
'''
diabetes=np.loadtxt("data/diabetes.csv", delimiter=",", dtype=np.float32)
print(diabetes)
xdata=diabetes[:,0:-1]
ydata=diabetes[:,[-1]]
print(xdata, ydata)