# -*- coding: utf-8 -*-
import unittest

from


class TestAzimuth(unittest.TestCase):
    def test_azimuth_degree_90(self):
        self.assertEqual(degree(90), 'Восточный')

if __name__ == '__main__':
    unittest.main()