import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

len1 = 1.0  
len2 = 1.0

# Path equation
def given_curve(t):
    x = np.cos(t)
    y = 0.5*np.sin(t)
    return x, y

def in_kin(x, y):
    c2 = (x*2 + y2 - len12 - len2*2) / (2 * len1 * len2)
    s2 = np.sqrt(1 - c2**2)

    q1 = np.arctan2(y, x) - np.arctan2(len2 * s2, len1 + len2 * c2)
    q2 = np.arctan2(s2, c2)

    return q1, q2

time_interval = 100
t_values = np.linspace(0, 2 * np.pi, time_interval)

#Animation
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)

link1, = ax.plot([], [], 'b-', lw=2)
link2, = ax.plot([], [], 'g-', lw=2)
endpoint, = ax.plot([], [], 'ro')
trace, = ax.plot([], [], 'r--', lw=1)  

trace_x = []  
trace_y = []  

def fun_animation(frame):
    t = t_values[frame]
    x_d, y_d = given_curve(t)
    q1, q2 = in_kin(x_d, y_d)
    q1_deg = np.degrees(q1)
    q2_deg = np.degrees(q2)
    
    if 35 <= q1_deg <= 145 and 35 <= q2_deg <= 145:
        x1 = len1 * np.cos(q1)
        y1 = len1 * np.sin(q1)
        
        x2 = x1 + len2 * np.cos(q1 + q2)
        y2 = y1 + len2 * np.sin(q1 + q2)

        link1.set_data([0, x1], [0, y1])
        link2.set_data([x1, x2], [y1, y2])
        endpoint.set_data(x2, y2)

        trace_x.append(x2)  # Add x coordinate to trace list
        trace_y.append(y2)  # Add y coordinate to trace list
        trace.set_data(trace_x, trace_y)  # Update trace plot

    return link1, link2, endpoint, trace 

ani = FuncAnimation(fig, fun_animation, frames=time_interval, blit=True)
plt.show()
