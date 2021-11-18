import cartesian_grid_walk as walk
import polar_grid_walk as polar_walk

import matplotlib.pyplot as plt
import numpy as np

"""
#Showing last positions over a time forms a normal distribution
lasts = []
for i in range(10000):
    mywalk = walk.random_walk_1d(1000)
    lasts.append(mywalk.path[-1])
    if i%300 == 0: print('On: ', i)

unique = np.arange(np.min(lasts), np.max(lasts))
counts = np.array([np.count_nonzero(lasts == i, axis = 0)
                           for i in unique])
unique, counts = np.array([unique]), np.array([counts])
result = np.concatenate((unique.T, counts.T), axis = 1)

plt.plot(result[:, 0], result[:, 1])
plt.title('Counts of last positions')
plt.xlabel('Last Positions')
plt.ylabel('Counts')
plt.show()
"""
#==========================================================
"""
#Showing asymmetry in p and q creates a net drift velocity
mywalk = walk.random_walk_1d(10000, probs = [0.45, 0.55])
mywalk.plot_path()
"""
#==========================================================
"""
#Asymmetric walk counts plot
lasts = []
for i in range(10000):
    mywalk = walk.random_walk_1d(1000, probs = [0.47, 0.53])
    lasts.append(mywalk.path[-1])
    if i%300 == 0: print('On: ', i)

unique = np.arange(np.min(lasts), np.max(lasts))
counts = np.array([np.count_nonzero(lasts == i, axis = 0)
                           for i in unique])
unique, counts = np.array([unique]), np.array([counts])
result = np.concatenate((unique.T, counts.T), axis = 1)

plt.plot(result[:, 0], result[:, 1])
plt.title('Counts of last positions')
plt.xlabel('Last Positions')
plt.ylabel('Counts')
plt.show()
"""
#==========================================================

#Polar 2d walker
mywalk = polar_walk.random_walk_2d(1000)
mywalk.plot_path()

#==========================================================
"""
lasts = []
for i in range(10000):
    mywalk = walk.random_walk_2d(1000)
    lasts.append(mywalk.path[-1])
    if i%300 == 0: print('On: ', i)

unique = np.arange(np.min(lasts), np.max(lasts))
counts = np.array([np.count_nonzero(lasts == i, axis = 0)
                           for i in unique])
result = np.concatenate((np.array([unique]).T, counts), axis = 1)

plt.bar(result[:, 0], result[:, 1])
plt.title('Counts of last positions')
plt.xlabel('Last Positions')
plt.ylabel('Counts')
plt.show()
"""
#==========================================================
"""
lasts = []
for i in range(10000):
    mywalk = walk.random_walk_3d(1000)
    lasts.append(mywalk.path[-1])
    if i%300 == 0: print('On: ', i)

unique = np.arange(np.min(lasts), np.max(lasts))
counts = np.array([np.count_nonzero(lasts == i, axis = 0)
                           for i in unique])
result = np.concatenate((np.array([unique]).T, counts), axis = 1)

plt.bar(result[:, 0], result[:, 1])
plt.title('Counts of last positions')
plt.xlabel('Last Positions')
plt.ylabel('Counts')
plt.show()
"""
