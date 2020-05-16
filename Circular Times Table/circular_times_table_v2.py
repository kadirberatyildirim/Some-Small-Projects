import numpy as np
from matplotlib import pyplot as plt
from matplotlib.widgets import Slider

def timesTableLines():
    lines = []
    for i in range(len(dots)):
        lines.append(startAndFinish = [dots[i], dots[dot_indexes[i] * times % N]])

theta = np.linspace(0, 2*np.pi, 1000) #Required for drawing circle
N = 10
dots = np.arange(0, np.pi * 2, 2 * np.pi / N)
dot_indexes = np.arange(N)
times = 2 #Some interesting points: 2, 3, 21, 29, 33, 34, 51, 67, 68, 80, 99

plt.style.use('dark_background') #Some nice fonts: ggplot, dark_background
fig = plt.figure()
ax = fig.add_subplot(111)
ax.axis('off')
#Next two lines make the figure fullscreen
mng = plt.get_current_fig_manager()
mng.window.state('zoomed')
#Next two lines keep the aspect ratio of figure
ax = plt.gca() #you first need to get the axis handle
ax.set_aspect(1) #sets the height to width ratio to 1.5. 

ax_N  = plt.axes([0.1, 0.05, 0.25, 0.025])
ax_times = plt.axes([0.1, 0.10, 0.25, 0.025])
slider_N  = Slider(ax_N,  'N',  10, 400, valinit = N, valstep = 1)
slider_times = Slider(ax_times, 'Times', 2, 200, valinit = times, valstep = 1)

#Initializing plots
ax.plot(np.cos(theta), np.sin(theta), linewidth = 1) #Plots circle
#Plots dots on the circle, with their numbers
for i in range(len(dots)):
    ax.annotate(str(dot_indexes[i]), (-np.cos(dots[i]), np.sin(dots[i])))
ax.scatter(-np.cos(dots), np.sin(dots), linewidth = 1)
#Plots lines between dots
for i in range(len(dots)):
    startAndFinish = [dots[i], dots[dot_indexes[i] * times % N]]
    lines, = ax.plot(-np.cos(startAndFinish), np.sin(startAndFinish), linewidth = 1)

def update(val):
    ax.clear()
    ax.plot(np.cos(theta), np.sin(theta), linewidth = 1) #Plots circle
    ax.axis('off')
    
    N = int(slider_N.val)
    dots = np.arange(0, np.pi * 2, 2 * np.pi / N)
    dot_indexes = np.arange(N)
    times = int(slider_times.val)
    
    for i in range(len(dots)):
        ax.annotate(str(dot_indexes[i]), (-np.cos(dots[i]), np.sin(dots[i])))
    ax.scatter(-np.cos(dots), np.sin(dots), linewidth = 1)
    for i in range(len(dots)):
        startAndFinish = [dots[i], dots[dot_indexes[i] * times % N]]
        lines, = ax.plot(-np.cos(startAndFinish), np.sin(startAndFinish), linewidth = 1)

    fig.canvas.draw_idle() 
    
slider_N.on_changed(update)
slider_times.on_changed(update)

plt.show()
