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

    @unittest.skip('pending feature')
    def test_address_find(self):
        system = classes.System(width=500., height=200., cell_length=2.)
        system.add_particle(classes.Particle())
        system.particles[0].state[:2] = [1.4, 1.2 ]
        self.assertEqual([0,0], system.particles[0].cell_address())
        system.particles[0].state[:2] = [201.4, 201.2 ]
        self.assertEqual([100,0], system.particles[0].cell_address())
        system.particles[0].state[:2] = [15.4, 11.2 ]
        self.assertEqual([7,5], system.particles[0].cell_address())

    @unittest.skip('pending feature')
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
        system.particles[4].state[:2] = [3.5, 5.5]
        system.populate_cell_list()
        self.assertEqual(2, len(system.particles[0].neighbors))
        self.assertEqual(3, len(system.particles[1].neighbors))
        self.assertEqual([0,2,3], sorted(system.particles[1].neighbors))
        self.assertEqual(0, len(system.particles[4].neighbors))

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

    @unittest.skip('pending feature')
    def test_make_cell_list():
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
        self.assertEqual([1],system.cell_list[2][1])
        self.assertEqual([2,3],system.cell_list[4][2])

    @unittest.skip('pending feature')
    def test_drag_force():
        system = classes.System(drag_coeff = .1)
        state = numpy.array([0.0, 0.0, 0.0, random.random()*50-25])
        force = system.drag_force(state)
        self.assertEqual(0.0, force[2])
        self.assertTrue(0.0 > force[3]*state[3])

    @unittest.skip('pending feature')
    def test_confinement_force():
        pass
        # system = classes.System(buffer_width = 10., height=100.)

if __name__ == '__main__':
    unittest.main()
