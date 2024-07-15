# Example 12.11
import numpy as np 
import matplotlib.pyplot as plt 

x = np.linspace(-np.pi, np.pi, 50) 
y1 = np.sin(x)
plt.plot(x, y1, color = 'blue', marker = "s", label='Sin') 
plt.legend()
plt.show()
