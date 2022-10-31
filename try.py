import numpy as np
import math
import matplotlib.animation as animation
import matplotlib.pyplot as plt


def init():
    global angle, V, dt, maxT, V, T, g, l
    maxT = 25
    dt = 0.0001
    T = 0
    V = 0.3
    angle = 3
    l = 1
    g = 9.8

    time = np.linspace(0, maxT, int(maxT/dt))
    t = []
    # cord = []
    res = []
    
    
fig = plt.figure()
axis = plt.axes(xlim=(0, 25),ylim=(-math.pi ,math.pi))
line, = axis.plot([], [])

# fig, ax = plt.subplots()
# line, = ax.plot([], [])
# fig1, bx = plt.subplots()
# ax.plot(time, res)
# bx.plot(res, cord)
# ax.set_xlabel(r'$\sin(\alpha)$')
# ax.set_ylabel("a")
# ax.legend()
# bx.get_xaxis().set_visible(False)
# bx.get_yaxis().set_visible(False)
# fig.set_figheight(4)
# fig.set_figwidth(10)
# fig1.set_figheight(4)
# fig1.set_figwidth(10)

def update(frame_number):
    # cord.append(-V)
    x = l * angle
    a = -g * math.sin(angle)
    dx = V * dt
    angle = (x + dx) / l
    if angle >= math.pi or angle <= -math.pi:
        angle *= -1
    V += a * dt
    res.append(angle)
    t.append(frame_number*dt)
    line.set_data(t, res)


anim = animation.FuncAnimation(fig, update, frames=1000, interval=200, repeat=False, init_func=init)

plt.show()
