import unittest
import src.Task_16


class Task16TestCase(unittest.TestCase):
	def test_solution(self):
		self.assertEqual(src.Task_16.solution(), None)

	def test_main(self):
		self.assertEqual(src.Task_16.main(), None)


if __name__ == "__main__":
	unittest.main()
