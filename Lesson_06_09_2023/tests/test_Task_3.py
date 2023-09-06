import unittest
import src.Task_3


class MyTestCase(unittest.TestCase):
    def test_solution_1(self):
        self.assertEqual(src.Task_3.solution([-9, 4, -10, 5, -8, 7, -5, 1, -6, 10]), (7, 0))

    def test_solution_2(self):
        self.assertEqual(src.Task_3.solution([-9, 10, -3, -4, 4, -5, -1, 2, 1, 7]), (9, 8))

    def test_main_arg_1(self):
        self.assertEqual(src.Task_3.main("-9 4 -10 5 -8 7 -5 1 -6 10"), "ARRAY: [-9, 4, -10, 5, -8, 7, -5, 1, -6, 10]\nAFTER MIN: 7\nAFTER MAX: 0")

    def test_main_arg_2(self):
        self.assertEqual(src.Task_3.main("-9 10 -3 -4 4 -5 -1 2 1 7"), "ARRAY: [-9, 10, -3, -4, 4, -5, -1, 2, 1, 7]\nAFTER MIN: 9\nAFTER MAX: 8")

    def test_main_args_1(self):
        self.assertEqual(src.Task_3.main("-9", "4", "-10", "5", "-8", "7", "-5", "1", "-6", "10"), "ARRAY: [-9, 4, -10, 5, -8, 7, -5, 1, -6, 10]\nAFTER MIN: 7\nAFTER MAX: 0")

    def test_main_args_2(self):
        self.assertEqual(src.Task_3.main("-9", "10", "-3", "-4", "4", "-5", "-1", "2", "1", "7"), "ARRAY: [-9, 10, -3, -4, 4, -5, -1, 2, 1, 7]\nAFTER MIN: 9\nAFTER MAX: 8")


if __name__ == "__main__":
    unittest.main()
