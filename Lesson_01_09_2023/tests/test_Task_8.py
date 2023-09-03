import unittest
import src.Task_8


class Task8TestCase(unittest.TestCase):
	def test_solution(self):
		self.assertEqual(src.Task_8.solution(5, 2, 5, 14), (7, 4, 5))

	def test_main_arg(self):
		self.assertEqual(src.Task_8.main("5 2 5 14"), "Red: 7.0\nYellow: 4.0\nGreen: 5.0")

	def test_main_args(self):
		self.assertEqual(src.Task_8.main("5", "2", "5", "14"), "Red: 7.0\nYellow: 4.0\nGreen: 5.0")

	def test_main_kwargs(self):
		self.assertEqual(src.Task_8.main(a="5", b="2", c="5", n="14"), "Red: 7.0\nYellow: 4.0\nGreen: 5.0")


if __name__ == "__main__":
	unittest.main()
