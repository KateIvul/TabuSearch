
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from TSPReader import Coordinate

class Plotter():
    def __init__(self, coord_list):
        self.coord_list = coord_list
        self.xlim = max([c.x for c in self.coord_list])
        self.ylim = max([c.y for c in self.coord_list])
        self.xcoords = [c.x for c in self.coord_list]
        self.ycoords = [c.y for c in self.coord_list]
        self.fig, self.ax = plt.subplots()
        self.xdata, self.ydata = [], []
        self.ax.plot(self.xcoords, self.ycoords, 'bo')
        self.ax.annotate('Start', xy=[self.xcoords[0],self.ycoords[0]],)
        for i, c in enumerate(self.coord_list[1:-1]):
            self.ax.annotate('({},{})'.format(c.x,c.y), xy=[c.x,c.y],)

        (self.ln,) = plt.plot([], [], 'ro-',mfc='b')
        self.ani = FuncAnimation(self.fig, self._update, frames=[[c.x, c.y] for c in self.coord_list],
                        init_func=self._init_plot, blit=True, interval=500, repeat=False)

    def _init_plot(self):
        self.ax.set_xlim(0, self.xlim)
        self.ax.set_ylim(0, self.ylim)
        return (self.ln,)


    def _update(self, frame):

        self.previous_city = frame
        self.xdata.append(frame[0])
        self.ydata.append(frame[1])
        self.ln.set_data(self.xdata, self.ydata)
        #self.annotation = plt.annotate('({},{})'.format(frame[0],frame[1]), xy=(frame[0],frame[1]))
        return (self.ln,)

    def plot(self):
        plt.show()


if __name__ == '__main__':
    pass
