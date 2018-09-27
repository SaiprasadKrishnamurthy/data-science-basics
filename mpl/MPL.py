import matplotlib.pyplot as plt
import numpy as np

print()
y = np.random.randint(100, size=50)
x = np.arange(50)
plt.plot(x, y)
plt.ylabel("Numbers")
plt.xlabel("Interest")
plt.title("Something")
plt.grid()
plt.show()
