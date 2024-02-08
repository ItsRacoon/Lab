program 1:

import matplotlib.pyplot as plt
temperature=[21, 45, 32, 22, 19, 20]
date=["jan1", "jan2", "jan3", "jan4", "jan5", "jan6"]
plt.plot(temperature,date,color='red')
plt.xlabel("temperature",color='pink')
plt.ylabel("date",color='pink')
plt.show()



program 2:

import pandas as pd 
import matplotlib.pyplot as plt 
df=pd.read_csv("melasales.csv")
df.plot(kind='line',color=['red','blue', 'brown'])
plt.title("MELA SALES REPOT")
plt.xlabel("days")
plt.ylabel("sales in Rs")
plt.show()

import pandas as pd 
import matplotlib.pyplot as plt 
df=pd.read_csv("melasales.csv")
df.plot(kind='bar',color=['red','blue', 'brown'])
plt.title("MELA SALES REPOT")
plt.xlabel("days")
plt.ylabel("sales in Rs")
plt.show()



program 3:

import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("min_max.csv",usecols=["ANNUAL_MAX", "ANNUAL_MIN"])
df=pd.DataFrame(data)
df.plot(kind='hist', y="ANNUAL_MAX", title="ANNUAL MAXIMUM TEMPERATURE", color=['blue', 'orange'])
plt.xlabel=("Temperature")
plt.ylabel=("Number of times")
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("min_max.csv",usecols=["ANNUAL_MAX"])
df=pd.DataFrame(data)
df.plot(kind='hist', y="ANNUAL_MAX", title="ANNUAL MAXIMUM TEMPERATURE", color=['blue'])
plt.xlabel=("Temperature")
plt.ylabel=("Number of times")
plt.show()



program 4:

import pandas as pd
import matplotlib.pyplot as plt 
data=pd.read_csv("resort.csv")
df=pd.DataFrame(data)
df.plot(kind='box', x='year')
plt.title("RESORT RATINGS")
plt.ylabel("ratings")
plt.xlabel("year")
plt.show()

import pandas as pd
import matplotlib.pyplot as plt 
data=pd.read_csv("resort.csv")
df=pd.DataFrame(data)
df.plot(kind='box', x='year', vert = False)
plt.title("RESORT RATINGS")
plt.ylabel("ratings")
plt.xlabel("year")
plt.show()



program 5:

import numpy as np 
import matplotlib.pyplot as plt
sales_in_Rs = np.array([40000, 45000, 48000, 50000, 100000])
discount=np.array([10, 20, 30, 40, 50])
plt.scatter(x=discount, y=sales_in_Rs)
plt.title("DISCOUNT VS SALES")
plt.xlabel=("Discount")
plt.ylabel=("Sales")
plt.show()

import numpy as np 
import matplotlib.pyplot as plt
sales_in_Rs = np.array([40000, 45000, 48000, 50000, 100000])
discount=np.array([10, 20, 30, 40, 50])
size=discount*10
plt.scatter(x=discount, y=sales_in_Rs, s=size, color='red', linewidths=3, marker='*', edgecolor='blue')
plt.title("DISCOUNT VS SALES")
plt.xlabel=("Discount")
plt.ylabel=("Sales")
plt.show()


