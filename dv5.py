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
