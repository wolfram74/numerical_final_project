import numpy
import random
import math
def rand_vec():
    return numpy.array([random.random() for ele in range(4)])

def vec_as_string(vec):
    return ("%f "*len(vec)+'\n') % tuple(vec)

for i in range(200):
    output = open('../produced_data/tht_0.6666_w_137/t_%03d.txt' % i, 'w')
    for part_num in range(1,8):
        r = part_num/7.
        tht = math.pi*i/100
        output.write(vec_as_string(
            [r*math.cos(tht*part_num), r*math.sin(tht*part_num), .3, .4]
            ))

