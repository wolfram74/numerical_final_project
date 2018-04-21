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


class SystemTest(unittest.TestCase):
    def test_meta(self):
        self.assertTrue(True)
    def test_add_particle(self):
        system = classes.System()
        system.add_particle(Particle())
        self.assertEqual(1, len(system.particles))
        system.add_particle(Particle())
        self.assertEqual(2, len(system.particles))
