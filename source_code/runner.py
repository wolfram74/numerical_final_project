import classes
import data_utils
import class_helpers
import time
import numpy

def relaxer():
    system = classes.System(
        width=500./3., height=200./3.0,
        drag_coeff=.1, buffer_width=10.0,
        frequency=138
        )
    class_helpers.system_with_density(system, .25)
    loops = 2
    print(len(system.particles))
    t0 = time.time()
    data_utils.save_state_data(system)
    for i in xrange(loops):
        system.time_step()
        data_utils.save_state_data(system)
    tf = time.time()
    delta_t = tf-t0
    print('%f to take %d steps' % (delta_t, loops))

def continue_system():
    system = classes.System(
        width=500./3., height=200./3.0,
        drag_coeff=.01, buffer_width=10.0,
        frequency=1., time =0.0,
        amplitude=3.,
        step_size=.05
        )
    last_state= './w_167_h_77.txt'
    class_helpers.load_state_from_file(system, last_state)
    loops = 200
    print(len(system.particles))
    t0 = time.time()
    data_utils.save_state_data(system)
    for i in xrange(loops):
        system.time_step()
        # data_utils.save_state_data(system)
        print(
            i,
            system.time,
            system.kinetic_energy(),
            system.potential_energy()
            )
    tf = time.time()
    delta_t = tf-t0
    print('%f to take %d steps' % (delta_t, loops))

def energy_plot(freq, angle):
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
    print(len(system.particles))
    t0 = time.time()
    data_out = open('../produced_data/energy_plots/%s.txt'%str(system), 'w')
    for i in xrange(loops):
        system.time_step()
        PE = system.potential_energy()
        KE = system.kinetic_energy()
        TE = PE+KE
        T = system.time
        data_vals = (T, PE, KE, TE)
        print(
            i,
            T, TE
            )
        # print('%f %f %f %f\n' % data_vals)
        data_out.write('%f %f %f %f\n' % data_vals)
    tf = time.time()
    delta_t = tf-t0
    print('%f to take %d steps' % (delta_t, loops))

if __name__ == '__main__':
    # relaxer()
    # continue_system()
    for freq in numpy.linspace(1, 5, num=5, endpoint=True):
        for angle in numpy.linspace(0, numpy.pi/2, num=5, endpoint=True):
            print(freq, angle)
            energy_plot(freq, angle)
