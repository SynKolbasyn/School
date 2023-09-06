import unittest
import src.Task_2


class MyTestCase(unittest.TestCase):
    def test_solution_1(self):
        self.assertEqual(src.Task_2.solution([[-3, 3, -2, -4], [-2, 0, -1, -3], [-4, 2, 0, 4], [-4, -2, 3, -1]]), (-11, [-13, 0]))

    def test_solution_2(self):
        self.assertEqual(src.Task_2.solution([[0, -2, -1], [1, 3, -2], [3, -1, 2]]), (8, [4, -1]))

    def test_main_args_1(self):
        self.assertEqual(src.Task_2.main("-3 3 -2 -4", "-2 0 -1 -3", "-4 2 0 4", "-4 -2 3 -1"), "MATRIX:\n[-3, 3, -2, -4]\n[-2, 0, -1, -3]\n[-4, 2, 0, 4]\n[-4, -2, 3, -1]\nSUMM: -11\nODD SUMM: [-13, 0]")

    def test_main_args_2(self):
        self.assertEqual(src.Task_2.main("0 -2 -1", "1 3 -2", "3 -1 2"), "MATRIX:\n[0, -2, -1]\n[1, 3, -2]\n[3, -1, 2]\nSUMM: 8\nODD SUMM: [4, -1]")


if __name__ == "__main__":
    unittest.main()
