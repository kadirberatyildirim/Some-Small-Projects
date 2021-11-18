import cartesian_grid_walk as walk
import polar_grid_walk as polar_walk
"""
#Example walk

mywalk = walk.random_walk_2d(1000, step_size = 1)
mywalk.plot_path(lib = 'plotly')
#mywalk.barplot_occurences()
"""
mywalk = walk.random_walk_3d(10000)
mywalk.plot_path()
"""
for i in range(1000):
    mywalk = walk.random_walk_2d(10000)
    """