"""
TO DO!
"""
import numpy as np

class random_walk_2d():
    def __init__(self, steps, init_pos = (0, 0), step_size = 1):
        self.steps = steps
        self.path = [init_pos]
        self.step_size = step_size

        self.allowed_steps = ['+r', '-r', '+theta', '-theta']
        self.occurences = []

        self.walk()

    def walk(self):
        for i in range(self.steps):
            self.path.append(self.calc_next())
        self.path = np.array(self.path)
        self.occurences = self.calc_occurences()

    def calc_next(self):
        cur_step = np.random.choice(self.allowed_steps)
        if cur_step == '+r': next_pos = (self.path[-1][0] + self.step_size, self.path[-1][1])
        elif cur_step == '-r': next_pos = (self.path[-1][0] - self.step_size, self.path[-1][1])
        elif cur_step == '+theta': next_pos = (self.path[-1][0], self.path[-1][1] + self.step_size)
        elif cur_step == '-theta': next_pos = (self.path[-1][0], self.path[-1][1] - self.step_size)
        return next_pos

    def path_to_pandas(self):
        import pandas as pd
        return pd.DataFrame(self.path, columns = ['x', 'y'])

    def plot_path(self):
        import matplotlib.pyplot as plt
        plt.polar(self.path[:, 1], self.path[:, 0], xunits = 'degrees')
        plt.title('2D Random Walk with {} Steps'.format(self.steps))
        plt.show()

    def calc_occurences(self):
        unique = range(np.min(self.path), np.max(self.path))
        counts = np.array([np.count_nonzero(self.path == i, axis = 0)
                           for i in unique])
        return np.concatenate((np.array([unique]).T, counts), axis = 1)

    def occurences_to_pandas(self):
        import pandas as pd
        return pd.DataFrame(self.occurences, columns = ['values', 'x_count', 'y_count'])

    def plot_occurences(self):
        import matplotlib.pyplot as plt
        plt.plot(self.occurences[:, 0], self.occurences[:, 1], label = 'x count')
        plt.plot(self.occurences[:, 0], self.occurences[:, 2], label = 'y count')
        plt.legend()
        plt.title('Occurences')
        plt.xlabel('Unique values')
        plt.ylabel('Counts')
        plt.show()

    def barplot_occurences(self):
        import matplotlib.pyplot as plt
        plt.bar(self.occurences[:, 0], self.occurences[:, 1], label = 'x count')
        plt.bar(self.occurences[:, 0], self.occurences[:, 2], label = 'y count')
        plt.legend()
        plt.title('Occurences')
        plt.xlabel('Unique values')
        plt.ylabel('Counts')
        plt.show()

class random_walk_3d():
    def __init__(self, steps, init_pos = (0, 0, 0)):
        self.steps = steps
        self.path = [init_pos]

        self.allowed_steps = ['+x', '-x', '+y', '-y', '+z', '-z']
        self.occurences = []

        self.walk()

    def walk(self):
        for i in range(self.steps):
            self.path.append(self.calc_next())
        self.path = np.array(self.path)
        self.occurences = self.calc_occurences()

    def calc_next(self):
        cur_step = np.random.choice(self.allowed_steps)
        if cur_step == '+x':
            next_pos = (self.path[-1][0] + 1, self.path[-1][1], self.path[-1][2])
        elif cur_step == '-x':
            next_pos = (self.path[-1][0] - 1, self.path[-1][1], self.path[-1][2])
        elif cur_step == '+y':
            next_pos = (self.path[-1][0], self.path[-1][1] + 1, self.path[-1][2])
        elif cur_step == '-y':
            next_pos = (self.path[-1][0], self.path[-1][1] - 1, self.path[-1][2])
        elif cur_step == '+z':
            next_pos = (self.path[-1][0], self.path[-1][1], self.path[-1][2] + 1)
        elif cur_step == '-z':
            next_pos = (self.path[-1][0], self.path[-1][1], self.path[-1][2] - 1)
        return next_pos

    def path_to_pandas(self):
        import pandas as pd
        return pd.DataFrame(self.path, columns = ['x', 'y', 'z'])

    def plot_path(self):
        import matplotlib.pyplot as plt
        from mpl_toolkits.mplot3d import Axes3D
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        ax.plot(self.path[:, 0], self.path[:, 1], self.path[:, 2])

        plt.title('3D Random Walk with {} Steps'.format(self.steps))
        plt.show()
        
    def calc_occurences(self):
        unique = range(np.min(self.path), np.max(self.path))
        counts = np.array([np.count_nonzero(self.path == i, axis = 0)
                           for i in unique])
        return np.concatenate((np.array([unique]).T, counts), axis = 1)

    def occurences_to_pandas(self):
        import pandas as pd
        return pd.DataFrame(self.occurences, columns = ['values', 'x_count', 'y_count'])

    def plot_occurences(self):
        import matplotlib.pyplot as plt
        plt.plot(self.occurences[:, 0], self.occurences[:, 1], label = 'x count')
        plt.plot(self.occurences[:, 0], self.occurences[:, 2], label = 'y count')
        plt.plot(self.occurences[:, 0], self.occurences[:, 3], label = 'z count')
        plt.legend()
        plt.title('Occurences')
        plt.xlabel('Unique values')
        plt.ylabel('Counts')
        plt.show()

    def barplot_occurences(self):
        import matplotlib.pyplot as plt
        plt.bar(self.occurences[:, 0], self.occurences[:, 1], label = 'x count')
        plt.bar(self.occurences[:, 0], self.occurences[:, 2], label = 'y count')
        plt.bar(self.occurences[:, 0], self.occurences[:, 3], label = 'z count')
        plt.legend()
        plt.title('Occurences')
        plt.xlabel('Unique values')
        plt.ylabel('Counts')
        plt.show()
        
