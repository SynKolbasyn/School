import unittest
import src.Task_14


class Task14TestCase(unittest.TestCase):
	def test_solution(self):
		self.assertEqual(src.Task_14.solution(), None)

	def test_main(self):
		self.assertEqual(src.Task_14.main(), None)


if __name__ == "__main__":
	unittest.main()
