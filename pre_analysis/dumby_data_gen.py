import numpy
import random

def rand_vec():
    return numpy.array([random.random() for ele in range(4)])

def vec_as_string(vec):
    return ("%f "*len(vec)+'\n') % tuple(vec)

for i in range(5):
    output = open('../produced_data/tht_0.6666_w_137/t_%d.txt' % i, 'w')
    for part_num in range(4):
        output.write(vec_as_string(rand_vec()))

