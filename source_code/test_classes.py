import unittest
import numpy
import random

import classes

class ParticleTest(unittest.TestCase):
    def setUp(self):
        self.random4vec_1 = numpy.array([random.random()*4.-2. for i in range(4)])
        self.random4vec_2 = numpy.array([random.random()*4.-2. for i in range(4)])

    def test_meta(self):
        self.assertTrue(True)

    def test_seperation_calc(self):
        particle = classes.Particle()
        seperation = particle.sepVec(self.random4vec_1, self.random4vec_2)
        self.assertEqual(2, len(seperation))
        deltax = self.random4vec_1[0] - self.random4vec_2[0]
        self.assertEqual(deltax, seperation[0])

    def test_address_find(self):
        system = classes.System(width=500., height=200., cell_length=2.)
        system.add_particle(classes.Particle())
        system.particles[0].state[:2] = [1.4, 1.2 ]
        self.assertEqual([0,0], system.particles[0].cell_address())
        system.particles[0].state[:2] = [201.4, 1.2 ]
        self.assertEqual([100,0], system.particles[0].cell_address())
        system.particles[0].state[:2] = [15.4, 11.2 ]
        self.assertEqual([7,5], system.particles[0].cell_address())

    def test_get_neighbors(self):
        system = classes.System(width=6., height=7., cell_length=1.)
        system.add_particle(classes.Particle())
        system.add_particle(classes.Particle())
        system.add_particle(classes.Particle())
        system.add_particle(classes.Particle())
        system.add_particle(classes.Particle())
        system.particles[0].state[:2] = [2.5, 2.5]
        system.particles[1].state[:2] = [1.5, 2.5]
        system.particles[2].state[:2] = [0.5, 3.5]
        system.particles[3].state[:2] = [5.5, 3.5]
        system.particles[4].state[:2] = [3.5, 6.5]
        system.populate_cell_list()
        self.assertEqual(2, len(system.particles[0].neighbor_ids))
        self.assertEqual(3, len(system.particles[1].neighbor_ids))
        self.assertEqual([0,2,3], sorted(system.particles[1].neighbor_ids))
        self.assertEqual(0, len(system.particles[4].neighbor_ids))

    def test_interaction_force(self):
        particle = classes.Particle()
        force = particle.interaction_force(self.random4vec_1, self.random4vec_2)
        seperation = particle.sepVec(self.random4vec_1, self.random4vec_2)
        sep_angle = numpy.arctan2(seperation[0], seperation[1])
        force_angle = numpy.arctan2(force[2], force[3])
        self.assertTrue(abs(sep_angle-force_angle) < 10.**-3)
        force2 = particle.interaction_force(
            2*self.random4vec_1, 2*self.random4vec_2
            )
        self.assertTrue( numpy.linalg.norm(force)>numpy.linalg.norm(force2))

class SystemTest(unittest.TestCase):
    def test_meta(self):
        self.assertTrue(True)
    def test_add_particle(self):
        system = classes.System()
        system.add_particle(classes.Particle())
        self.assertEqual(1, len(system.particles))
        self.assertEqual(system, system.particles[0].system)

        system.add_particle(classes.Particle())
        self.assertEqual(2, len(system.particles))

    def test_make_cell_list(self):
        system = classes.System(width=500., height=200., cell_length=2.)
        system.add_particle(classes.Particle())
        system.add_particle(classes.Particle())
        system.add_particle(classes.Particle())
        system.add_particle(classes.Particle())
        system.particles[0].state[:2] = [1.4, 1.2 ]
        system.particles[1].state[:2] = [4.4, 3.2 ]
        system.particles[2].state[:2] = [8.4, 5.2 ]
        system.particles[3].state[:2] = [9.4, 5.7 ]
        system.populate_cell_list()
        self.assertEqual([0],system.cell_list[0][0])
        self.assertEqual([1],system.cell_list[1][2])
        self.assertEqual([2,3],system.cell_list[2][4])

    def test_drag_force(self):
        system = classes.System(drag_coeff = .1)
        state = numpy.array([0.0, 0.0, 0.0, random.random()*50-25])
        force = system.drag_force(state)
        self.assertEqual(0.0, force[2])
        self.assertTrue(0.0 > force[3]*state[3])

    def test_confinement_force(self):
        system = classes.System(buffer_width = 10., height=100.)
        bottom_state = numpy.array([0.0,5.0, 0, 0])
        force_bottom = system.confinement_force(bottom_state)
        self.assertTrue(force_bottom[3]>0)
        top_state = numpy.array([0.0,95.0, 0, 0])
        force_top = system.confinement_force(top_state)
        self.assertTrue(force_top[3]<0)
        middle_state = numpy.array([0.0,50.0, 0, 0])
        force_middle = system.confinement_force(middle_state)
        self.assertTrue(abs(force_middle[3]) < abs(force_top[3]))

    def test_string_form(self):
        system = classes.System()
        self.assertTrue('Rh' in str(system))

class TimeStepTest(unittest.TestCase):
    def setUp(self):
        self.random4vec_1 = numpy.array([random.random()*4.-2. for i in range(4)])
        self.random4vec_2 = numpy.array([random.random()*4.-2. for i in range(4)])
        self.system = classes.System(width=500, height=200, buffer_width=10, drag_coeff=.01, step_size=0.01, cell_length=2.)
        self.system.add_particle(classes.Particle())

    def test_drag_over_time(self):
        self.system.drag_coeff = .1
        vx_0 = 10.0
        self.system.particles[0].state[:] = [20.0, 100.0, vx_0, 0]
        for i in range(100):
            self.system.time_step()
        self.assertTrue(vx_0 > self.system.particles[0].state[2])
        self.assertTrue(0.0 <= self.system.particles[0].state[2])

    def test_confinement_over_time(self):
        self.system.add_particle(classes.Particle())
        y_0 = 1.0
        self.system.particles[0].state[1] =  y_0
        self.system.particles[1].state[1] =  self.system.height-y_0
        for i in range(100):
            self.system.time_step()
        self.assertTrue(y_0 < self.system.particles[0].state[1])
        self.assertTrue(self.system.height-y_0 > self.system.particles[1].state[1])

    def test_interaction_over_time(self):
        self.system.add_particle(classes.Particle())
        self.system.particles[0].state[:2] = [20.0, 100.0]
        self.system.particles[1].state[:2] = (
            self.system.particles[0].state[:2]+
            self.random4vec_1[:2]/2
            )
        sep_init = self.system.particles[0].sepVec(
            self.system.particles[0].state,
            self.system.particles[1].state
            )
        for i in range(100):
            self.system.time_step()
        sep_final = self.system.particles[0].sepVec(
            self.system.particles[0].state,
            self.system.particles[1].state
            )
        self.assertTrue(
            numpy.linalg.norm(sep_final) > numpy.linalg.norm(sep_init)
            )

    def test_periodicity_cosntraint(self):
        vx_0 = 10.0
        steps = 100
        self.system.particles[0].state[:] = [499.0, 100.0, vx_0, 0]
        for i in range(steps):
            self.system.time_step()
        self.assertTrue(
            self.system.particles[0].state[0] < self.system.width
            )
        self.assertTrue(
            self.system.particles[0].state[0] < vx_0*self.system.step_size*steps
            )

if __name__ == '__main__':
    unittest.main()
