import matplotlib.pyplot as pyplot
import matplotlib.animation as animation

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
    print(field.get_array())
    # field.set_data(x_vals, y_vals)

if __name__=='__main__':
    data = load_data('../produced_data/tht_0.6666_w_137/t_0.txt')
    # print(data)
    # scatter_plot(data)
    print(field)
    print(field.get_array())
    pyplot.show()
    frame_init()
    pyplot.show

