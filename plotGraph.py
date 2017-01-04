import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import time

style.use("ggplot")

figure = plt.figure()
subpl = figure.add_subplot(1,1,1)

def animate(i):
    pullData = open("twitter-out.txt","r").read()
    lines = pullData.split('\n')

    xl = []
    yl = []

    x = 0
    y = 0

    for l in lines[-100:]:
        x += 1
        if "pos" in l:
            y += 1
        elif "neg" in l:
            y -= 1

        xl.append(x)
        yl.append(y)
        
    subpl.clear()
    subpl.plot(xl,yl)
anim = animation.FuncAnimation(figure, animate, interval=1000)
plt.show()