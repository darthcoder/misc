import numpy as np
import matplotlib.pyplot as plt
from mpmath import mp


r = np.linspace(1e-9, 10e-9, 100)

mp.dps = 70

force = 24*(2*(r**7) - (r**13))/(r**91)

# print(force)

plt.plot(r, force)

plt.show()