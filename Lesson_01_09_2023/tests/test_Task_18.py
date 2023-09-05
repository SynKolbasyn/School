import unittest
import src.Task_18


class Task18TestCase(unittest.TestCase):
	def test_solution_1(self):
		self.assertEqual(src.Task_18.solution(10), "123456789")

	def test_solution_2(self):
		self.assertEqual(src.Task_18.solution(3), "123")

	def test_solution_3(self):
		self.assertEqual(src.Task_18.solution(11), "12345678910")

	def test_main_arg_1(self):
		self.assertEqual(src.Task_18.main("10"), "123456789")

	def test_main_arg_2(self):
		self.assertEqual(src.Task_18.main("3"), "123")

	def test_main_arg_3(self):
		self.assertEqual(src.Task_18.main("11"), "12345678910")

	def test_main_kwargs_1(self):
		self.assertEqual(src.Task_18.main(n="10"), "123456789")

	def test_main_kwargs_2(self):
		self.assertEqual(src.Task_18.main(n="3"), "123")

	def test_main_kwargs_3(self):
		self.assertEqual(src.Task_18.main(n="11"), "12345678910")


if __name__ == "__main__":
	unittest.main()
