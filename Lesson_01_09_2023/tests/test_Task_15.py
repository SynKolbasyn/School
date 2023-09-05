import unittest
import src.Task_15


class Task15TestCase(unittest.TestCase):
	def test_solution_1(self):
		self.assertEqual(src.Task_15.solution(1, 1, 1), 3)

	def test_solution_2(self):
		self.assertEqual(src.Task_15.solution(3, 4, 4), 1)

	def test_main_arg_1(self):
		self.assertEqual(src.Task_15.main("1 1 1"), 3)

	def test_main_arg_2(self):
		self.assertEqual(src.Task_15.main("3 4 4"), 1)

	def test_main_args_1(self):
		self.assertEqual(src.Task_15.main("1", "1", "1"), 3)

	def test_main_args_2(self):
		self.assertEqual(src.Task_15.main("3", "4", "4"), 1)

	def test_main_kwargs_1(self):
		self.assertEqual(src.Task_15.main(b="1", c="1", d="1"), 3)

	def test_main_kwargs_2(self):
		self.assertEqual(src.Task_15.main(c="3", b="4", d="4"), 1)


if __name__ == "__main__":
	unittest.main()
