import pandas as pd
import matplotlib.pyplot as plt
dt=pd.read_csv("hotel.csv")

dt.plot(kind='box',x='year',vert=False)
plt.xlabel("year")
plt.ylabel("Hotels")
plt.show()