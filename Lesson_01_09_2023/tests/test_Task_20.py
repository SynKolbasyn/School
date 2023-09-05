import unittest
import src.Task_20


class Task20TestCase(unittest.TestCase):
	def test_solution_1(self):
		self.assertEqual(src.Task_20.solution("aaabbbccc"), "aaa bbb ccc")

	def test_solution_2(self):
		self.assertEqual(src.Task_20.solution("abc"), "a b c")

	def test_main_arg_1(self):
		self.assertEqual(src.Task_20.main("aaabbbccc"), "aaa bbb ccc")

	def test_main_arg_2(self):
		self.assertEqual(src.Task_20.main("abc"), "a b c")


if __name__ == "__main__":
	unittest.main()
