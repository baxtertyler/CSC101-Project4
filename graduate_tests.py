# Project 4 – Graduate Rate (2017-2018)
# Name:
# Instructor: Dr. S. Einakian
# Section:

# unittest cases for graduate rate will include here
import unittest
from graduate_funcs import *


class TestCases(unittest.TestCase):

    g1 = Graduate(3250, "major1", (5, 10), (6, 11), (7, 12))
    g1_ = Graduate(3250, "major1_", (5, 10), (6, 11), (7, 12))
    g2 = Graduate(3450, "major2", (10, 15), (11, 16), (12, 17))
    g3 = Graduate(3650, "major3", (15, 20), (16, 21), (17, 22))
    g4 = Graduate(3850, "major4", (20, 25), (21, 26), (22, 27))
    g5 = Graduate(3850, "major5", (25, 30), (26, 31), (27, 32))

    print(g1 == g1_)
    print(g1 == g2)

    print(g1)

    def test_find_total_avg(self):
        grad_list1 = [Graduate(3250, "major1", (5, 10), (6, 11), (7, 12)),
                      Graduate(3450, "major2", (10, 15), (11, 16), (12, 17)),
                      Graduate(3650, "major3", (15, 20), (16, 21), (17, 22)),
                      Graduate(3850, "major4", (15, 21), (16, 21), (17, 22))]
        grad_list2 = [Graduate(3250, "major5", (12, 15), (11, 16), (12, 17)),
                      Graduate(3450, "major6", (15, 20), (16, 21), (18, 22)),
                      Graduate(3650, "major7", (24, 25), (22, 26), (22, 27)),
                      Graduate(3850, "major8", (20, 25), (21, 26), (22, 27))]
        grad_list3 = [Graduate(3250, "major9", (15, 23), (16, 29), (17, 34)),
                      Graduate(3450, "major10", (20, 24), (21, 26), (22, 27)),
                      Graduate(3650, "major11", (5, 10), (9, 15), (7, 12)),
                      Graduate(3850, "major12", (10, 15), (13, 16), (12, 19))]

        self.assertEqual(find_total_avg(grad_list1),
                         [(51, 8.5), (81, 13.5), (111, 18.5), (112, 18.666666666666668), (355, 14.791666666666666)])
        self.assertEqual(find_total_avg(grad_list2),
                         [(83, 13.833333333333334), (112, 18.666666666666668),
                          (146, 24.333333333333332), (141, 23.5), (482, 20.083333333333332)])
        self.assertEqual(find_total_avg(grad_list3),
                         [(134, 22.333333333333332), (140, 23.333333333333332),
                          (58, 9.666666666666666), (85, 14.166666666666666), (417, 17.375)])

    def test_find_graduation_rate(self):
        g1 = Graduate(3250, "major1", (5, 10), (6, 11), (7, 12))
        g2 = Graduate(3450, "major2", (10, 15), (11, 16), (12, 17))
        g3 = Graduate(3650, "major3", (15, 20), (16, 21), (17, 22))
        self.assertEqual(find_graduation_rate(g1), (18, 33))
        self.assertEqual(find_graduation_rate(g2), (33, 48))
        self.assertEqual(find_graduation_rate(g3), (48, 63))

    def test1(self):
        lst = ["hello world", "goodbye"]
        print(lst)
        for line in lst:
            for char in line:
                print(char + " ")


# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
