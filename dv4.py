import pandas as pd
import matplotlib.pyplot as plt 
data=pd.read_csv("resort.csv")
df=pd.DataFrame(data)
df.plot(kind='box', x='year')
plt.title("RESORT RATINGS")
plt.ylabel("ratings")
plt.xlabel("year")
plt.show()


/2

import pandas as pd
import matplotlib.pyplot as plt 
data=pd.read_csv("resort.csv")
df=pd.DataFrame(data)
df.plot(kind='box', x='year', vert = False)
plt.title("RESORT RATINGS")
plt.ylabel("ratings")
plt.xlabel("year")
plt.show()
