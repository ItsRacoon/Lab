import pandas as pd 
import matplotlib.pyplot as plt 
df=pd.read_csv("melasales.csv")
df.plot(kind='line',color=['red','blue', 'brown'])
plt.title("MELA SALES REPOT")
plt.xlabel("days")
plt.ylabel("sales in Rs")
plt.show()

//  2


import pandas as pd 
import matplotlib.pyplot as plt 
df=pd.read_csv("melasales.csv")
df.plot(kind='bar',color=['red','blue', 'brown'])
plt.title("MELA SALES REPOT")
plt.xlabel("days")
plt.ylabel("sales in Rs")
plt.show()
