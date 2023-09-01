import unittest
import src.Task_13


class Task13TestCase(unittest.TestCase):
	def test_solution(self):
		self.assertEqual(src.Task_13.solution(), None)

	def test_main(self):
		self.assertEqual(src.Task_13.main(), None)


if __name__ == "__main__":
	unittest.main()
