import matplotlib.pyplot as plt
import numpy as np

discount = [10, 20, 30, 40, 50]
sale_in_rupees = [40000, 45000, 48000, 50000, 100000]  # Corrected the missing value in sale_in_rupees

# 1-------------------------------
plt.scatter(discount, sale_in_rupees)
plt.xlabel("Discount")
plt.ylabel("Sales")
plt.show()

# 2--------------------------------
dis = np.array(discount)
sales = np.array(sale_in_rupees)
size = dis * 10  # Adjusting marker size based on discount

plt.scatter(x=dis, y=sales, s=size)
plt.xlabel("Discount")
plt.ylabel("Sales")
plt.title("Scatter Plot with Size Adjustment")
plt.show()
