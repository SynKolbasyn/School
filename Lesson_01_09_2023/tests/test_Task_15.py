import unittest
import src.Task_15


class Task15TestCase(unittest.TestCase):
	def test_solution(self):
		self.assertEqual(src.Task_15.solution(), None)

	def test_main(self):
		self.assertEqual(src.Task_15.main(), None)


if __name__ == "__main__":
	unittest.main()
