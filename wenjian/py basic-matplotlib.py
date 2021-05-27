import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(2, 2, sharex=True, sharey=True)
for i in range(2):
    for j in range(2):
        axes[i, j].hist(np.random.randn(500), bins=50, color="r", alpha=0.7)
plt.subplots_adjust(wspace=0, hspace=0)
plt.figure()
data=np.random.randn(30).cumsum()
plt.show()

