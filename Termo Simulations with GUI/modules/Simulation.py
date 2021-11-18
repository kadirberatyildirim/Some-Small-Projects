
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import animation
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.animation import TimedAnimation
import numpy as np
from itertools import combinations
from modules.Particle import Particle
"""


"""
#plot style
plt.style.use('dark_background')

class Simulate(FigureCanvasQTAgg):
    def __init__(self, N, radius, parent=None):
        self.N, self.radius = N, radius
        self.dt = 0.05
        self.ns = []
        
        self.init_particles()
        self.setUp()
        
        FigureCanvasQTAgg.__init__(self, self.fig)

    def init_particles(self):
        self.particles = []
        #Find a random non-overlapping initial position for all particles
        for i in range(self.N):
            while True:
                x, y = self.radius + (1 - 2*self.radius) * np.random.random(2)
                vr = 0.1 * np.random.random() + 0.05
                vphi = 2*np.pi * np.random.random()
                vx, vy = vr * np.cos(vphi), vr * np.sin(vphi)
                particle = Particle(x, y, vx, vy, self.radius)

                for p in self.particles:
                    if p.overlap(particle):
                        break
                else:
                    self.particles.append(particle)
                    break
            
    def check_collision(self):
        def elastic_collision(p1, p2):
            m1, m2 = p1.radius**2, p2.radius**2
            M = m1 + m2
            r1, r2 = p1.r, p2.r
            d = np.linalg.norm(r1 - r2)**2
            v1, v2 = p1.v, p2.v
            u1 = v1 - 2*m2 / M * np.dot(v1-v2, r1-r2) / d * (r1 - r2)
            u2 = v2 - 2*m1 / M * np.dot(v2-v1, r2-r1) / d * (r2 - r1)
            p1.v, p2.v = u1, u2

        pairs = combinations(range(self.N), 2)
        for i, j in pairs:
            if self.particles[i].overlap(self.particles[j]):
                elastic_collision(self.particles[i], self.particles[j])
    
    def count_n(self):
        n = 0
        for particle in self.particles:
            if particle.x <= 0.5:
                n += 1
        self.ns.append(n)
        print("N = %d, n = %d, n' = %d"%(self.N, n, self.N - n))
    
    def anim_init(self):
        self.circles, artists = [], []
        for particle in self.particles:
            self.circles.append(particle.draw(self.ax))
        return self.circles

    def animate(self, i):
        """
        Animation goes as follows:
            -Particles are moved to their next positions
            -Their corresponding circle object's center is updated
            -Collisions are then checked, if any, velocities are
                updated via check_collision -> elastic_collision
            -Particles on the left side are counted for the text
                to be updated via update_text method
        """
        artists = []
        for i, p in enumerate(self.particles):
            p.move(self.dt)
            self.circles[i].center = p.r
        self.check_collision()
        self.count_n()
        return self.circles
    
    def setUp(self, save = False):
        #This function starts the animation window with its initials
        self.fig = plt.figure()
        self.fig.set_dpi(100)
        self.fig.set_size_inches(7, 6.5)

        self.ax = plt.axes(xlim=(0, 1), ylim=(0, 1))

        self.ax.set_title('')

        #A fixed dotted line in the middle
        dotted_line = plt.Line2D((0.5, 0.5), (0, 1), lw = 1., 
                                 ls='-.',
                                 alpha=0.5)
        self.ax.add_line(dotted_line)

    def start(self):
        anim = animation.FuncAnimation(self.fig, self.animate, init_func = self.anim_init, 
                                       frames = 360, interval = 20, blit = True)
        plt.show()
        
if __name__ == '__main__':
    particles = 100
    radius = 0.01
    sim = Simulate(particles, radius)
    sim.setUp(save = True)
