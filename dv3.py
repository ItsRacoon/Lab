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
