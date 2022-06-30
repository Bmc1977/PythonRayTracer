import unittest
from vector import Vector3


class TestVectors(unittest.TestCase):
    def setUp(self):
        self.v1 = Vector3(1.0, -2.0, -2.0)
        self.v2 = Vector3(3.0, 6.0, 9.0)
        self.v3 = Vector3(4.0, 4.0, 7.0)
        self.v4 = Vector3(-2.0, -8.0, -11.0)
        self.v5 = Vector3(2.0, -4.0, -4.0)
        self.v6 = Vector3(0.5, -1.0, -1.0)

    def test_magnitude(self):
        self.assertEqual(self.v1.magnitude(), 3)

    def test_add(self):
        self.assertEqual(self.v1 + self.v2, self.v3)

    def test_subtract(self):
        self.assertEqual(self.v1 - self.v2, self.v4)

    def test_multiply(self):
        self.assertEqual(self.v1 * 2, self.v5)

    def test_rmultiply(self):
        self.assertEqual(2 * self.v1, self.v5)

    def test_divide(self):
        self.assertEqual(self.v1 / 2, self.v6)
