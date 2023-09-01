import unittest
import src.Task_5


class Task5TestCase(unittest.TestCase):
	def test_solution(self):
		self.assertEqual(src.Task_5.solution(), None)

	def test_main(self):
		self.assertEqual(src.Task_5.main(), None)


if __name__ == "__main__":
	unittest.main()
