import os
import re
from matplotlib import pyplot

def load_data(file_address):
    file_data = open(file_address, 'r')
    states = []
    # print(file_address)
    for line in file_data:
        # print(line, line.split())
        values = [float(ele) for ele in line.split()]
        states.append(values[:])
    return states



def ke_from_file(file_name):
    data = load_data(file_name)
    ke = 0.0
    for particle in data:
        ke += particle[3]**2+particle[2]**2
    return ke/len(data)


def time_from_file_name(file_name):
    matches = re.search('t_(\d*\.\d*)', file_name)
    return matches.group(1)

def find_files(folder):
    files = os.listdir(folder)
    usable_files = filter(lambda x: 'Store' not in x, files)
    address = map(lambda x: "%s/%s" %(folder, x), usable_files)
    return address


def ke_vs_t():
    run_name = 'A_0.000_W_138.000_Th_0.000_Rh_0.250'
    state_data = find_files('../produced_data/%s' % run_name)
    t_vals = []
    ke_vals = []
    for state in state_data:
        t_vals.append(time_from_file_name(state))
        ke_vals.append(ke_from_file(state))
    pyplot.plot(t_vals, ke_vals)
    pyplot.show()

if __name__=='__main__':
    ke_vs_t()
