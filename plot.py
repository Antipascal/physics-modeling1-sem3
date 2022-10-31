# %%

import numpy as np
import math
import matplotlib.pyplot as plt

maxT = 25
dt = 0.00001
V = 0.3
angle = 3
l = 1
g = 9.8

time = np.linspace(0, maxT, int(maxT/dt))
cord = []
res = []

for t in time:
    cord.append(V)
    x = l * angle
    a = -g * math.sin(angle)
    dx = V * dt
    angle = (x + dx) / l
    if angle >= math.pi or angle <= -math.pi:
        angle *= -1
    V += a * dt
    res.append(angle * 180 / math.pi)


fig, ax = plt.subplots()
fig1, bx = plt.subplots()
ax.plot(time, res)
bx.plot(res, cord)
bx.grid()

ax.set_xlabel("T, сек")
ax.set_ylabel(r"$Отклонение, ^o$")

bx.set_xlabel(r"$Отклонение, ^o$")
bx.set_ylabel("Угловая скорость, м/с")

fig.set_figheight(4)
fig.set_figwidth(10)
fig1.set_figheight(4)
fig1.set_figwidth(10)

plt.show()

# %%
