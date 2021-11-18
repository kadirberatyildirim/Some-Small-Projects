"""
Position format is (x, y) for 2D walks, (x, y, z) for 3D walks.
"""
import numpy as np

class random_walk_1d():
    def __init__(self, steps, init_pos = 0, step_size = [1, 1], probs = [0.5, 0.5]):
        self.steps = steps
        self.path = [init_pos]
        self.step_size_x_pos, self.step_size_x_neg = step_size
        self.probs = probs
        
        self.allowed_steps = ['+x', '-x']
        self.occurences = []

        self.walk()

    def walk(self):
        for i in range(self.steps):
            self.path.append(self.calc_next())
        self.path = np.array(self.path)
        self.occurences = self.calc_occurences()

    def calc_next(self):
        cur_step = np.random.choice(self.allowed_steps, p = self.probs)
        if cur_step == '+x': next_pos = self.path[-1] + self.step_size_x_pos
        elif cur_step == '-x': next_pos = self.path[-1] - self.step_size_x_neg
        return next_pos

    def plot_path(self):
        import matplotlib.pyplot as plt

        plt.plot(self.path, range(len(self.path)), label = 'walk', color = 'g')
        plt.title('1D Random Walk')
        plt.xlabel('x position')
        plt.ylabel('steps')

        plt.plot((self.path[-1], self.path[-1]), (0, len(self.path)), 'r--', label = 'last position')

        plt.legend()
        plt.show()

    def calc_occurences(self):
        unique = np.arange(np.min(self.path), np.max(self.path), self.step_size)
        counts = np.array([np.count_nonzero(self.path == i, axis = 0)
                           for i in unique])
        unique, counts = np.array([unique]), np.array([counts])
        return np.concatenate((unique.T, counts.T), axis = 1)

    def plot_occurences(self):
        import matplotlib.pyplot as plt

        plt.plot(self.occurences[:, 0], self.occurences[:, 1], label = 'x count')
        plt.legend()
        plt.title('Occurences')
        plt.xlabel('Unique values')
        plt.ylabel('Counts')
        plt.show()

    def barplot_occurences(self):
        import matplotlib.pyplot as plt

        plt.bar(self.occurences[:, 0], self.occurences[:, 1], label = 'x count')
        plt.legend()
        plt.title('Occurences')
        plt.xlabel('Unique values')
        plt.ylabel('Counts')
        plt.show()

class random_walk_2d():
    def __init__(self, steps, init_pos = (0, 0), step_size = 1, probs = [0.33, 0.33, 0.33, 0.33]):
        self.steps = steps
        self.path = [init_pos]
        self.step_size = step_size
        #Prob. calc. if given probabilities do not add to 1 for an axis, remaining is added as a stop move
        if probs[0] + probs[1] == 1: self.probs_x = probs[:2]
        else:
            remain = 1 - (probs[0] + probs[1]) 
            self.probs_x = [probs[0], remain, probs[1]]
        if probs[2] + probs[3] == 1: self.probs_y = probs[2:4]
        else:
            remain = 1 - (probs[2] + probs[3]) 
            self.probs_y = [probs[2], remain, probs[3]]

        if len(self.probs_x) == 3: self.allowed_steps_x = ['+x', '0', '-x']
        else: self.allowed_steps_x = ['+x', '-x']
        if len(self.probs_y) == 3: self.allowed_steps_y = ['+y', '0', '-y']
        else: self.allowed_steps_y = ['+y', '-y']
            
        self.occurences = []

        self.walk()

    def walk(self):
        for i in range(self.steps):
            self.path.append(self.calc_next())
        self.path = np.array(self.path)
        self.occurences = self.calc_occurences()

    def calc_next(self):
        cur_step_x = np.random.choice(self.allowed_steps_x, p = self.probs_x)
        if cur_step_x == '+x': next_pos_x = self.path[-1][0] + self.step_size
        elif cur_step_x == '-x': next_pos_x = self.path[-1][0] - self.step_size
        else: next_pos_x = self.path[-1][0]
        
        cur_step_y = np.random.choice(self.allowed_steps_y, p = self.probs_y)
        if cur_step_y == '+y': next_pos_y = self.path[-1][1] + self.step_size
        elif cur_step_y == '-y': next_pos_y = self.path[-1][1] - self.step_size
        else: next_pos_y = self.path[-1][1]

        next_pos = (next_pos_x, next_pos_y)
        return next_pos

    def path_to_pandas(self):
        import pandas as pd
        return pd.DataFrame(self.path, columns = ['x', 'y'])

    def plot_path(self, lib = 'mpl'):
        if lib == 'mpl' or 'matplotlib':
            import matplotlib.pyplot as plt
            plt.plot(self.path[:, 0], self.path[:, 1])
            plt.title('2D Random Walk with {} Steps'.format(self.steps))
            plt.show()
        """
        elif lib == 'plotly':
            import plotly.express as px
            df_path = self.path_to_pandas()
            fig = px.line(df_path, x = "x", y = "y", title = '2D Random Walk with {} Steps'.format(self.steps))
            fig.show()
        """
    def calc_occurences(self):
        unique = np.arange(np.min(self.path), np.max(self.path), self.step_size)
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

class random_walk_3d(): #TO DO! Spacial random walker in 3D!
    def __init__(self, steps, init_pos = (0, 0, 0), step_size = 1):
        self.steps = steps
        self.path = [init_pos]
        self.step_size = step_size

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
            next_pos = (self.path[-1][0] + self.step_size, self.path[-1][1], self.path[-1][2])
        elif cur_step == '-x':
            next_pos = (self.path[-1][0] - self.step_size, self.path[-1][1], self.path[-1][2])
        elif cur_step == '+y':
            next_pos = (self.path[-1][0], self.path[-1][1] + self.step_size, self.path[-1][2])
        elif cur_step == '-y':
            next_pos = (self.path[-1][0], self.path[-1][1] - self.step_size, self.path[-1][2])
        elif cur_step == '+z':
            next_pos = (self.path[-1][0], self.path[-1][1], self.path[-1][2] + self.step_size)
        elif cur_step == '-z':
            next_pos = (self.path[-1][0], self.path[-1][1], self.path[-1][2] - self.step_size)
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
        unique = np.arange(np.min(self.path), np.max(self.path), self.step_size)
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
        
