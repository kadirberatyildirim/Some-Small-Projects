
from matplotlib.patches import Circle
import numpy as np

class Particle:
    def __init__(self, x, y, vx, vy, radius = 0.01):
        #Particle parameters
        self.r, self.v = np.array((x, y)), np.array((vx, vy))
        self.radius = radius

    @property
    def x(self):
        return self.r[0]
    @x.setter
    def x(self, value):
        self.r[0] = value
    @property
    def y(self):
        return self.r[1]
    @y.setter
    def y(self, value):
        self.r[1] = value
    @property
    def vx(self):
        return self.v[0]
    @vx.setter
    def vx(self, value):
        self.v[0] = value
    @property
    def vy(self):
        return self.v[1]
    @vy.setter
    def vy(self, value):
        self.v[1] = value

    def overlap(self, other):
        #Checks overlap of this particle with another
        return np.hypot(*(self.r - other.r)) < self.radius + other.radius

    def draw(self, ax):
        circle = Circle(xy = self.r, radius = self.radius)
        ax.add_patch(circle)
        return circle

    def move(self, dt):
        #Moves the particle to the next position in time by dt
        self.r += self.v * dt
        #Wall check
        if self.x - self.radius < 0:
            self.x = self.radius
            self.vx = -self.vx
        if self.x + self.radius > 1:
            self.x = 1-self.radius
            self.vx = -self.vx
        if self.y - self.radius < 0:
            self.y = self.radius
            self.vy = -self.vy
        if self.y + self.radius > 1:
            self.y = 1-self.radius
            self.vy = -self.vy
