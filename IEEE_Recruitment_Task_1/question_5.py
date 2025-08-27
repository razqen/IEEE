import numpy as np
import matplotlib.pyplot as plt
data=np.random.randn(1000)
plt.scatter(range(len(data)), data, alpha=0.6, s=20)
plt.xlabel("Index")
plt.ylabel("Value")
plt.title("Scatter Plot of 1000 Random Numbers")
plt.tight_layout()
plt.show(block=True)