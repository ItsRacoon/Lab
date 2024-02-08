import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("Min_max.csv",usecols=['ANNUAL - MIN','ANNUAL - MAX'])
df=pd.DataFrame(data)
#1------------------------------
df.plot(kind='hist',y='ANNUAL - MIN',title='Annual minimum temperature(1901-2017)')
plt.xlabel("temp")
plt.ylabel("number of times")

#2---------------------------------
df.plot(kind='hist',title='Annual minimum temperature(1901-2017)')
plt.xlabel("temp")
plt.ylabel("number of times")
plt.show()