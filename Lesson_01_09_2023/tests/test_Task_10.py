import unittest
import src.Task_10


class Task10TestCase(unittest.TestCase):
	def test_solution_1(self):
		self.assertTrue(src.Task_10.solution(0, 5, 2, 7))

	def test_solution_2(self):
		self.assertTrue(src.Task_10.solution(0, 0, 0, 0))

	def test_solution_3(self):
		self.assertTrue(src.Task_10.solution(-5, 0, 0, 5))

	def test_solution_4(self):
		self.assertFalse(src.Task_10.solution(-5, -2, 2, 5))

	def test_solution_5(self):
		self.assertFalse(src.Task_10.solution(2, 5, -5, -2))

	def test_main_arg_1(self):
		self.assertEqual(src.Task_10.main("0 5 2 7"), "YES")

	def test_main_arg_2(self):
		self.assertEqual(src.Task_10.main("0 0 0 0"), "YES")

	def test_main_arg_3(self):
		self.assertEqual(src.Task_10.main("-5 0 0 5"), "YES")

	def test_main_arg_4(self):
		self.assertEqual(src.Task_10.main("-5 -2 2 5"), "NO")

	def test_main_arg_5(self):
		self.assertEqual(src.Task_10.main("2 5 -5 -2"), "NO")

	def test_main_args_1(self):
		self.assertEqual(src.Task_10.main("0 5 2 7"), "YES")

	def test_main_args_2(self):
		self.assertEqual(src.Task_10.main("0", "0", "0", "0"), "YES")

	def test_main_args_3(self):
		self.assertEqual(src.Task_10.main("-5", "0", "0", "5"), "YES")

	def test_main_args_4(self):
		self.assertEqual(src.Task_10.main("-5", "-2", "2", "5"), "NO")

	def test_main_args_5(self):
		self.assertEqual(src.Task_10.main("2", "5", "-5", "-2"), "NO")

	def test_main_kwargs_1(self):
		self.assertEqual(src.Task_10.main("0 5 2 7"), "YES")

	def test_main_kwargs_2(self):
		self.assertEqual(src.Task_10.main(l1="0", r1="0", l2="0", r2="0"), "YES")

	def test_main_kwargs_3(self):
		self.assertEqual(src.Task_10.main(l1="-5", r1="0", l2="0", r2="5"), "YES")

	def test_main_kwargs_4(self):
		self.assertEqual(src.Task_10.main(l1="-5", r1="-2", l2="2", r2="5"), "NO")

	def test_main_kwargs_5(self):
		self.assertEqual(src.Task_10.main(l1="2", r1="5", l2="-5", r2="-2"), "NO")


if __name__ == "__main__":
	unittest.main()
