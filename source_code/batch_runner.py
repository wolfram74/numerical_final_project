import classes
import data_utils
import class_helpers
import time
import numpy
import multiprocessing

def energy_plot(f_tht_space):
    freq, angle = f_tht_space
    print(freq, angle)
    system = classes.System(
        width=500./3., height=200./3.0,
        drag_coeff=.01, buffer_width=10.0,
        frequency=freq, time =0.0, angle=angle,
        amplitude=3.,
        step_size=.1
        )
    last_state= './w_167_h_77.txt'
    class_helpers.load_state_from_file(system, last_state)
    loops = 200
    print(str(system))
    t0 = time.time()
    data_out = open('../produced_data/energy_plots/%s.txt'%str(system), 'w')
    for i in xrange(loops):
        system.time_step()
        PE = system.potential_energy()
        KE = system.kinetic_energy()
        TE = PE+KE
        T = system.time
        data_vals = (T, PE, KE, TE)
        print(str(system))
        print('%f %f %f %f\n' % data_vals)
        data_out.write('%f %f %f %f\n' % data_vals)
    tf = time.time()
    delta_t = tf-t0
    print('%f to take %d steps' % (delta_t, loops))
    return 4

if __name__ == '__main__':
    queries = []
    for freq in numpy.linspace(1.5, 4.5, num=4, endpoint=True):
        for angle in numpy.linspace(0, numpy.pi/2, num=5, endpoint=True):
            queries.append((freq, angle))
    pool = multiprocessing.Pool(4)
    pool.map(energy_plot, queries)
