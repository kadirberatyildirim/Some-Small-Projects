
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox
import numpy as np

def makeUnitCircle():
    theta = np.linspace(0, 2*np.pi, 1000) #Required for drawing circle
    plt.plot(np.cos(theta), np.sin(theta), linewidth = 1)

def putDotsOnCircle():
    for i in range(len(dots)):
        plt.annotate(str(dot_indexes[i]), (-np.cos(dots[i]), np.sin(dots[i])))
    plt.scatter(-np.cos(dots), np.sin(dots), linewidth = 1)

def drawTimesTableLines():
    for i in range(len(dots)):
        startAndFinish = [dots[i], dots[dot_indexes[i] * times % N]]
        plt.plot(-np.cos(startAndFinish), np.sin(startAndFinish), linewidth = 1)

def plotConfig():
    plt.axis('off')
    #Next two lines make the figure fullscreen
    mng = plt.get_current_fig_manager()
    mng.window.state('zoomed')
    #Next two lines keep the aspect ratio of figure
    ax = plt.gca() #you first need to get the axis handle
    ax.set_aspect(1) #sets the height to width ratio to 1.5. 
  
def update():
    plotConfig()
    makeUnitCircle()
    putDotsOnCircle()
    drawTimesTableLines()

N = 200
#times = 2 #Some interesting points: 2, 3, 21, 29, 33, 34, 51, 67, 68, 80, 99
dots = np.arange(0, np.pi * 2, 2 * np.pi / N)
dot_indexes = np.arange(N)

plt.style.use('dark_background') #Nice fonts: ggplot, dark_background

for i in range(2, 100):
    plt.clf()
    plt.annotate('Times: ' + str(i), (0.7, 1))
    times = i
    update()
    plt.pause(0.05)

plt.show()
