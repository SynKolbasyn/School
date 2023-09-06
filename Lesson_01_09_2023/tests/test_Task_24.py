import unittest
import src.Task_24


class Task24TestCase(unittest.TestCase):
	def test_solution_1(self):
		self.assertEqual(src.Task_24.solution("ABCDEFG", 1), "BDF")

	def test_solution_2(self):
		self.assertEqual(src.Task_24.solution("ABCDEFGH", 2), "CF")

	def test_main_arg_1(self):
		self.assertEqual(src.Task_24.main("ABCDEFG 1"), "BDF")

	def test_main_arg_2(self):
		self.assertEqual(src.Task_24.main("ABCDEFGH 2"), "CF")

	def test_main_args_1(self):
		self.assertEqual(src.Task_24.main("ABCDEFG", "1"), "BDF")

	def test_main_args_2(self):
		self.assertEqual(src.Task_24.main("ABCDEFGH", "2"), "CF")


if __name__ == "__main__":
	unittest.main()
