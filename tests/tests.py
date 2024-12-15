import unittest
from rubik import Rubik

class Tests(unittest.TestCase):

    def test(self):
        r = Rubik()
        print(r)
        r.scramble()
        print(r)