import unittest
import src.Task_22


class Task22TestCase(unittest.TestCase):
	def test_solution_1(self):
		self.assertTrue(src.Task_22.solution(((1, 2), (2, 1))))

	def test_solution_2(self):
		self.assertFalse(src.Task_22.solution(((1, 2), (1, 2))))

	def test_solution_3(self):
		self.assertTrue(src.Task_22.solution(((2, 1), (2, 1))))

	def test_main_args_1(self):
		self.assertEqual(src.Task_22.main("1 2", "2 1"), "YES")

	def test_main_args_2(self):
		self.assertEqual(src.Task_22.main("1 2", "1 2"), "NO")

	def test_main_args_3(self):
		self.assertEqual(src.Task_22.main("2 1", "2 1"), "YES")


if __name__ == "__main__":
	unittest.main()
