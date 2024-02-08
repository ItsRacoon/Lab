import pandas as pd
import matplotlib.pyplot as plt
dt=pd.read_csv("melasales.csv")
#1----------------------------------

dt.plot(kind='line',color=['red','blue','brown'])
plt.title("Mela sales")
plt.xlabel("days")
plt.ylabel("sales in rs")
plt.show()

#2----------------------------------

dt.plot(kind='line',x='days',color=['red','blue','brown'])
plt.title("Mela sales")
plt.xlabel("days")
plt.ylabel("sales in rs")
plt.show()