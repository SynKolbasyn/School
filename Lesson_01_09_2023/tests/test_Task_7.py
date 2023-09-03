import unittest
import src.Task_7


class Task7TestCase(unittest.TestCase):
	def test_solution_1(self):
		self.assertEqual(src.Task_7.solution(1, 2, 3), 1)

	def test_solution_2(self):
		self.assertEqual(src.Task_7.solution(1, 12, 3), 12)

	def test_solution_3(self):
		self.assertEqual(src.Task_7.solution(12, 12, 3), 12)

	def test_solution_4(self):
		self.assertEqual(src.Task_7.solution(9, 12, 3), 9)

	def test_solution_5(self):
		self.assertEqual(src.Task_7.solution(0, 0, 3), 0)

	def test_solution_6(self):
		self.assertEqual(src.Task_7.solution(-3, 0, 3), -3)

	def test_solution_7(self):
		self.assertEqual(src.Task_7.solution(-2, 1, 4), 1)

	def test_main_arg_1(self):
		self.assertEqual(src.Task_7.main("1 2 3"), 1)

	def test_main_arg_2(self):
		self.assertEqual(src.Task_7.main("1 12 3"), 12)

	def test_main_arg_3(self):
		self.assertEqual(src.Task_7.main("12 12 3"), 12)

	def test_main_arg_4(self):
		self.assertEqual(src.Task_7.main("9 12 3"), 9)

	def test_main_arg_5(self):
		self.assertEqual(src.Task_7.main("0 0 3"), 0)

	def test_main_arg_6(self):
		self.assertEqual(src.Task_7.main("-3 0 3"), -3)

	def test_main_arg_7(self):
		self.assertEqual(src.Task_7.main("-2 1 4"), 1)

	def test_main_args_1(self):
		self.assertEqual(src.Task_7.main("1", "2", "3"), 1)

	def test_main_args_2(self):
		self.assertEqual(src.Task_7.main("1", "12", "3"), 12)

	def test_main_args_3(self):
		self.assertEqual(src.Task_7.main("12", "12", "3"), 12)

	def test_main_args_4(self):
		self.assertEqual(src.Task_7.main("9", "12", "3"), 9)

	def test_main_args_5(self):
		self.assertEqual(src.Task_7.main("0", "0", "3"), 0)

	def test_main_args_6(self):
		self.assertEqual(src.Task_7.main("-3", "0", "3"), -3)

	def test_main_args_7(self):
		self.assertEqual(src.Task_7.main("-2", "1", "4"), 1)

	def test_main_kwargs_1(self):
		self.assertEqual(src.Task_7.main(a="1", b="2", d="3"), 1)

	def test_main_kwargs_2(self):
		self.assertEqual(src.Task_7.main(a="1", b="12", d="3"), 12)

	def test_main_kwargs_3(self):
		self.assertEqual(src.Task_7.main(a="12", b="12", d="3"), 12)

	def test_main_kwargs_4(self):
		self.assertEqual(src.Task_7.main(a="9", b="12", d="3"), 9)

	def test_main_kwargs_5(self):
		self.assertEqual(src.Task_7.main(a="0", b="0", d="3"), 0)

	def test_main_kwargs_6(self):
		self.assertEqual(src.Task_7.main(a="-3", b="0", d="3"), -3)

	def test_main_kwargs_7(self):
		self.assertEqual(src.Task_7.main(a="-2", b="1", d="4"), 1)


if __name__ == "__main__":
	unittest.main()
