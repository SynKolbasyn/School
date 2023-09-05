import unittest
import src.Task_16


class Task16TestCase(unittest.TestCase):
	def test_solution(self):
		self.assertEqual(src.Task_16.solution(10, 10, 7, 8), (5, "RRRRRRRUUUUUUUURRRUU"))

	def test_main_arg(self):
		self.assertEqual(src.Task_16.main("10 10 7 8"), "5\nRRRRRRRUUUUUUUURRRUU")

	def test_main_args(self):
		self.assertEqual(src.Task_16.main("10", "10", "7", "8"), "5\nRRRRRRRUUUUUUUURRRUU")

	def test_main_kwargs(self):
		self.assertEqual(src.Task_16.main(a="10", b="10", r="7", u="8"), "5\nRRRRRRRUUUUUUUURRRUU")


if __name__ == "__main__":
	unittest.main()
