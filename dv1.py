import matplotlib.pyplot as plt 
data =["12/11","10/11","16/11"]
temp =[84.5,98.6,100]
plt.xlabel("temp", color="red")
plt.ylabel("temp",color="blue")
plt.title("temp v/s  data",color="orange")
plt.plot(temp,data)
plt.grid()
plt.show()
