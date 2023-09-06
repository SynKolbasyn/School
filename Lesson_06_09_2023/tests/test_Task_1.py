import unittest
import src.Task_1


class Task1TestCase(unittest.TestCase):
    def test_solution_1(self):
        self.assertEqual(src.Task_1.solution([4, 0, 1, 2]), (4, 0))

    def test_solution_2(self):
        self.assertEqual(src.Task_1.solution([-10, 5, 7, 6, -9, -2, -5, 2, 3, 9]), (6, 2))

    def test_main_arg_1(self):
        self.assertEqual(src.Task_1.main("4 0 1 2"), "ARRAY: [4, 0, 1, 2]\nMAX: 4\nODD COUNT: 0")

    def test_main_arg_2(self):
        self.assertEqual(src.Task_1.main("-10 5 7 6 -9 -2 -5 2 3 9"), "ARRAY: [-10, 5, 7, 6, -9, -2, -5, 2, 3, 9]\nMAX: 6\nODD COUNT: 2")

    def test_main_args_1(self):
        self.assertEqual(src.Task_1.main("4", "0", "1", "2"), "ARRAY: [4, 0, 1, 2]\nMAX: 4\nODD COUNT: 0")

    def test_main_args_2(self):
        self.assertEqual(src.Task_1.main("-10", "5", "7", "6", "-9", "-2", "-5", "2", "3", "9"), "ARRAY: [-10, 5, 7, 6, -9, -2, -5, 2, 3, 9]\nMAX: 6\nODD COUNT: 2")


if __name__ == "__main__":
    unittest.main()
