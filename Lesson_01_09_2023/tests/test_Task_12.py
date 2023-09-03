import unittest
import src.Task_12


class Task12TestCase(unittest.TestCase):
	def test_solution_1(self):
		self.assertEqual(src.Task_12.solution("cat", "cat"), 1)

	def test_solution_2(self):
		self.assertEqual(src.Task_12.solution("pigeon", "pigeon"), 1)

	def test_solution_3(self):
		self.assertEqual(src.Task_12.solution("dog", "dog"), 1)

	def test_solution_4(self):
		self.assertEqual(src.Task_12.solution("cat", "pigeon"), 1)

	def test_solution_5(self):
		self.assertEqual(src.Task_12.solution("pigeon", "dog"), 1)

	def test_solution_6(self):
		self.assertEqual(src.Task_12.solution("pigeon", "cat"), 2)

	def test_solution_7(self):
		self.assertEqual(src.Task_12.solution("dog", "pigeon"), 2)

	def test_solution_8(self):
		self.assertEqual(src.Task_12.solution("cat", "dog"), 1)

	def test_solution_9(self):
		self.assertEqual(src.Task_12.solution("dog", "cat"), 2)

	def test_main_arg_1(self):
		self.assertEqual(src.Task_12.main("cat cat"), 1)

	def test_main_arg_2(self):
		self.assertEqual(src.Task_12.main("pigeon pigeon"), 1)

	def test_main_arg_3(self):
		self.assertEqual(src.Task_12.main("dog dog"), 1)

	def test_main_arg_4(self):
		self.assertEqual(src.Task_12.main("cat pigeon"), 1)

	def test_main_arg_5(self):
		self.assertEqual(src.Task_12.main("pigeon dog"), 1)

	def test_main_arg_6(self):
		self.assertEqual(src.Task_12.main("pigeon cat"), 2)

	def test_main_arg_7(self):
		self.assertEqual(src.Task_12.main("dog pigeon"), 2)

	def test_main_arg_8(self):
		self.assertEqual(src.Task_12.main("cat dog"), 1)

	def test_main_arg_9(self):
		self.assertEqual(src.Task_12.main("dog cat"), 2)

	def test_main_args_1(self):
		self.assertEqual(src.Task_12.main("cat", "cat"), 1)

	def test_main_args_2(self):
		self.assertEqual(src.Task_12.main("pigeon", "pigeon"), 1)

	def test_main_args_3(self):
		self.assertEqual(src.Task_12.main("dog", "dog"), 1)

	def test_main_args_4(self):
		self.assertEqual(src.Task_12.main("cat", "pigeon"), 1)

	def test_main_args_5(self):
		self.assertEqual(src.Task_12.main("pigeon", "dog"), 1)

	def test_main_args_6(self):
		self.assertEqual(src.Task_12.main("pigeon", "cat"), 2)

	def test_main_args_7(self):
		self.assertEqual(src.Task_12.main("dog", "pigeon"), 2)

	def test_main_args_8(self):
		self.assertEqual(src.Task_12.main("cat", "dog"), 1)

	def test_main_args_9(self):
		self.assertEqual(src.Task_12.main("dog", "cat"), 2)


if __name__ == "__main__":
	unittest.main()
