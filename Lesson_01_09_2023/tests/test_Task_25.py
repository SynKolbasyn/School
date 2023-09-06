import unittest
import src.Task_25


class Task25TestCase(unittest.TestCase):
	def test_solution_1(self):
		self.assertTrue(src.Task_25.solution("ABCDEF"))

	def test_solution_2(self):
		self.assertFalse(src.Task_25.solution("FEDCBA"))

	def test_solution_3(self):
		self.assertTrue(src.Task_25.solution("AbCdEf"))

	def test_solution_4(self):
		self.assertFalse(src.Task_25.solution("FeDcBa"))

	def test_main_arg_1(self):
		self.assertEqual(src.Task_25.main("ABCDEF"), "YES")

	def test_main_arg_2(self):
		self.assertEqual(src.Task_25.main("FEDCBA"), "NO")

	def test_main_arg_3(self):
		self.assertEqual(src.Task_25.main("AbCdEf"), "YES")

	def test_main_arg_4(self):
		self.assertEqual(src.Task_25.main("FeDcBa"), "NO")


if __name__ == "__main__":
	unittest.main()
