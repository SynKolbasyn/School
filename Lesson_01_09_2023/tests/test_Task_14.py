import unittest
import src.Task_14


class Task14TestCase(unittest.TestCase):
	def test_solution_1(self):
		self.assertEqual(src.Task_14.solution((123, 321, 442)), [123, 321])

	def test_solution_2(self):
		self.assertEqual(src.Task_14.solution((5483, 1836, 8126, 8253)), [1836])

	def test_main_arg_1(self):
		self.assertEqual(src.Task_14.main("123 321 442"), "123\n321")

	def test_main_arg_2(self):
		self.assertEqual(src.Task_14.main("5483 1836 8126 8253"), "1836")

	def test_main_args_1(self):
		self.assertEqual(src.Task_14.main("123", "321", "442"), "123\n321")

	def test_main_args_2(self):
		self.assertEqual(src.Task_14.main("5483", "1836", "8126", "8253"), "1836")


if __name__ == "__main__":
	unittest.main()
