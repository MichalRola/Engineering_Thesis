import os
import numpy as np
import matplotlib.pyplot as plt
import math

x = np.linspace(-4, 4, 1000)

GELU = 0.5 * x * (1 + np.tanh(np.sqrt(2 / math.pi) * (x + 0.044715 * x ** 3)))
# GELU = x/(1 + np.exp(-1.702*x))
ReLU = [max(x1, 0) for x1 in x]
ReLU = np.array(ReLU)

print(GELU.shape)
print(ReLU.shape)

plt.plot(x, GELU, 'k-', linewidth=2)
plt.plot(x, ReLU, 'k--', linewidth=2)
plt.legend(['GELU', 'ReLU'])
plt.xlim(-4, 4)
plt.ylim(-1, 3)
plt.yticks(np.linspace(-1, 3, 5))
plt.savefig(os.path.join(r'D:\Folders\_Engineering_Thesis\Papers\Images', 'GELU_vs_ReLU.png'))
plt.show()
