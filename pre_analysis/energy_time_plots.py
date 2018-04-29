import os
import re
from matplotlib import pyplot
import time

def load_data(file_address):
    file_data = open(file_address, 'r')
    states = []
    for line in file_data:
        values = [float(ele) for ele in line.split()]
        states.append(values[:])
    return states

def read_column(rank_2_tensor, col_num):
    return [row[col_num] for row in rank_2_tensor]


def ke_from_file(file_name):
    data = load_data(file_name)
    ke = 0.0
    for particle in data:
        ke += particle[3]**2+particle[2]**2
    return ke/len(data)


def time_from_file_name(file_name):
    matches = re.search('t_(\d*\.\d*)', file_name)
    return float(matches.group(1))

def find_files(folder):
    files = os.listdir(folder)
    usable_files = filter(lambda x: 'Store' not in x, files)
    address = map(lambda x: "%s/%s" %(folder, x), usable_files)
    return address


def ke_vs_t():
    run_name = 'A_3.000_W_1.000_Th_0.000_Rh_0.250'
    state_data = find_files('../produced_data/%s' % run_name)
    data_val = []
    t_vals = []
    ke_vals = []
    for state in state_data:
        data_val.append([time_from_file_name(state),ke_from_file(state)])
    data_val = sorted(data_val , key=(lambda ele: ele[0]))
    pyplot.plot(read_column(data_val, 0), read_column(data_val, 1))
    pyplot.show()

def energy_plots():
    run_name = 'A_3.000_W_1.000_Th_0.000_Rh_0.250.txt'
    # run_name = 'A_3.000_W_1.000_Th_0.000_Rh_0.250_si_0.05.txt'
    data_vals = load_data('../produced_data/energy_plots/%s' % run_name)
    print(len(data_vals))
    t_vals = read_column(data_vals, 0)
    PE_vals = read_column(data_vals, 1)
    KE_vals = read_column(data_vals, 2)
    TE_vals = read_column(data_vals, 3)
    pyplot.plot(t_vals, PE_vals)
    pyplot.plot(t_vals, KE_vals)
    pyplot.plot(t_vals, TE_vals)
    pyplot.savefig("%d.png" % int(time.time()))

if __name__=='__main__':
    # ke_vs_t()
    energy_plots()
