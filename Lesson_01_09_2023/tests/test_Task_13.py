import unittest
import src.Task_13


class Task13TestCase(unittest.TestCase):
	def test_solution_1(self):
		self.assertEqual(src.Task_13.solution(0, 0), 1)

	def test_solution_2(self):
		self.assertEqual(src.Task_13.solution(-1, 0), 1)

	def test_solution_3(self):
		self.assertEqual(src.Task_13.solution(-1, -1), -1)

	def test_solution_4(self):
		self.assertEqual(src.Task_13.solution(2, 2), 22)

	def test_solution_5(self):
		self.assertEqual(src.Task_13.solution(2, 3), 32)

	def test_solution_6(self):
		self.assertEqual(src.Task_13.solution(3, 2), 32)

	def test_main_arg_1(self):
		self.assertEqual(src.Task_13.main("0 0"), 1)

	def test_main_arg_2(self):
		self.assertEqual(src.Task_13.main("-1 0"), 1)

	def test_main_arg_3(self):
		self.assertEqual(src.Task_13.main("-1 -1"), -1)

	def test_main_arg_4(self):
		self.assertEqual(src.Task_13.main("2 2"), 22)

	def test_main_arg_5(self):
		self.assertEqual(src.Task_13.main("2 3"), 32)

	def test_main_arg_6(self):
		self.assertEqual(src.Task_13.main("3 2"), 32)

	def test_main_args_1(self):
		self.assertEqual(src.Task_13.main("0", "0"), 1)

	def test_main_args_2(self):
		self.assertEqual(src.Task_13.main("-1", "0"), 1)

	def test_main_args_3(self):
		self.assertEqual(src.Task_13.main("-1", "-1"), -1)

	def test_main_args_4(self):
		self.assertEqual(src.Task_13.main("2", "2"), 22)

	def test_main_args_5(self):
		self.assertEqual(src.Task_13.main("2", "3"), 32)

	def test_main_args_6(self):
		self.assertEqual(src.Task_13.main("3", "2"), 32)

	def test_main_kwargs_1(self):
		self.assertEqual(src.Task_13.main(x="0", y="0"), 1)

	def test_main_kwargs_2(self):
		self.assertEqual(src.Task_13.main(x="-1", y="0"), 1)

	def test_main_kwargs_3(self):
		self.assertEqual(src.Task_13.main(x="-1", y="-1"), -1)

	def test_main_kwargs_4(self):
		self.assertEqual(src.Task_13.main(x="2", y="2"), 22)

	def test_main_kwargs_5(self):
		self.assertEqual(src.Task_13.main(x="2", y="3"), 32)

	def test_main_kwargs_6(self):
		self.assertEqual(src.Task_13.main(x="3", y="2"), 32)


if __name__ == "__main__":
	unittest.main()
