# '''
import matplotlib.pyplot as pyplot
import matplotlib.animation as animation
import time
import math
import os
def load_data(file_address):
    file_data = open(file_address, 'r')
    positions = []
    for line in file_data:
        values = [float(ele) for ele in line.split()]
        positions.append(values[:2])
    return positions

def read_column(rank_2_tensor, col_num):
    return [row[col_num] for row in rank_2_tensor]

def scatter_plot(data):
    fig, axes = pyplot.subplots()
    x_vals = read_column(data,0)
    y_vals = read_column(data,1)
    axes.scatter(x_vals, y_vals)
    pyplot.show()

fig, axes = pyplot.subplots()
x_vals = [.5]
y_vals = [.2]
field = axes.scatter(x_vals, y_vals)

def frame_init():
    axes.set_ylim(0, 1)
    axes.set_xlim(0, 1)
    del x_vals[:]
    del y_vals[:]
    print('clearing?')
    axes.clear()
    axes.scatter([.4], [.3])
    # print(field.get_array())
    # field.set_data(x_vals, y_vals)

def frame_gen(frame_data):
    # del x_vals[:]
    # del y_vals[:]
    axes.clear()
    positions = load_data()
    x_vals=[math.cos(3.14*frame_num/100.0)]
    y_vals=[math.sin(3.14*frame_num/100.0)]
    axes.scatter(x_vals, y_vals)
    axes.set_ylim(-1, 1)
    axes.set_xlim(-1, 1)

def find_files(folder):
    files = os.listdir(folder)
    usable_files = filter(lambda x: 'ds' not in x, files)
    address = map(lambda x: "%s/%s" %(folder, x), usable_files)
    return address

if __name__=='__main__':
    data = load_data('../produced_data/tht_0.6666_w_137/t_0.txt')
    axes.set_ylim(-1, 1)
    axes.set_xlim(-1, 1)
    print(find_files('../produced_data/tht_0.6666_w_137'))
    # movie = animation.FuncAnimation(
    #     fig,
    #     frame_gen,
    #     frames=find_files('../produced_data/tht_0.6666_w_137')
    #     )
    # movie.save('test_circle.mp4')
# '''
'''
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

def main():
    numframes = 100
    numpoints = 10
    color_data = np.random.random((numframes, numpoints))
    x, y, c = np.random.random((3, numpoints))

    fig = plt.figure()
    scat = plt.scatter(x, y, c=c, s=100)
    print type(scat)
    ani = animation.FuncAnimation(fig, update_plot, frames=xrange(numframes),
                                  fargs=(color_data, scat))
    plt.show()

def update_plot(i, data, scat):
    print(len(data), data.shape, i)
    print(len(data[i]), data[i].shape)
    if i >0:
        data[i][0] = data[i-1][0]*.9
    scat.set_array(data[i])
    return scat


if __name__ == '__main__':
    main()
'''
