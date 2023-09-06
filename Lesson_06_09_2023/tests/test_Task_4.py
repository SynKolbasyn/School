import unittest
import src.Task_4


class MyTestCase(unittest.TestCase):
    def test_solution_1(self):
        self.assertEqual(src.Task_4.solution([[0, -1, 3, 4], [-4, 0, 2, 1], [2, -3, 1, -2], [-2, -3, 0, -4]]), (1, [0, 0, 0, 1]))

    def test_solution_2(self):
        self.assertEqual(src.Task_4.solution([[0, 1, -1], [3, 0, 1], [-2, 2, 1]]), (1, [0, 0, 1]))

    def test_main_args_1(self):
        self.assertEqual(src.Task_4.main("0 -1 3 4", "-4 0 2 1", "2 -3 1 -2", "-2 -3 0 -4"), "MATRIX:\n[0, -1, 3, 4]\n[-4, 0, 2, 1]\n[2, -3, 1, -2]\n[-2, -3, 0, -4]\nCOUNT: 1\nMINIMUM: [0, 0, 0, 1]")

    def test_main_args_2(self):
        self.assertEqual(src.Task_4.main("0 1 -1", "3 0 1", "-2 2 1"), "MATRIX:\n[0, 1, -1]\n[3, 0, 1]\n[-2, 2, 1]\nCOUNT: 1\nMINIMUM: [0, 0, 1]")


if __name__ == "__main__":
    unittest.main()
