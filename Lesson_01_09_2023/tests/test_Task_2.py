import unittest
import src.Task_2


class Task2TestCase(unittest.TestCase):
	def test_solution(self):
		self.assertEqual(src.Task_2.solution(10, 3, 5), 5.0)

	def test_main_args_0(self):
		self.assertEqual(src.Task_2.main("10 3 5"), 5.0)

	def test_main_args(self):
		self.assertEqual(src.Task_2.main("10", "3", "5"), 5.0)

	def test_main_kwargs(self):
		self.assertEqual(src.Task_2.main(s="10", v1="3", v2="5"), 5.0)


if __name__ == "__main__":
	unittest.main()
