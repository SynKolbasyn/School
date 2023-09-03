import unittest
import src.Task_6


class Task6TestCase(unittest.TestCase):
	def test_solution_1(self):
		self.assertEqual(src.Task_6.solution(10, 3), 3)

	def test_solution_2(self):
		self.assertEqual(src.Task_6.solution(10, 7), 3)

	def test_main_arg_1(self):
		self.assertEqual(src.Task_6.main("10 3"), 3)

	def test_main_arg_2(self):
		self.assertEqual(src.Task_6.main("10 7"), 3)

	def test_main_args_1(self):
		self.assertEqual(src.Task_6.main("10", "3"), 3)

	def test_main_args_2(self):
		self.assertEqual(src.Task_6.main("10", "7"), 3)

	def test_main_kwargs_1(self):
		self.assertEqual(src.Task_6.main(n="10", x="3"), 3)

	def test_main_kwargs_2(self):
		self.assertEqual(src.Task_6.main(n="10", x="7"), 3)


if __name__ == "__main__":
	unittest.main()
