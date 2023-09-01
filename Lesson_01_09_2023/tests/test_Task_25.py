import unittest
import src.Task_25


class Task25TestCase(unittest.TestCase):
	def test_solution(self):
		self.assertEqual(src.Task_25.solution(), None)

	def test_main(self):
		self.assertEqual(src.Task_25.main(), None)


if __name__ == "__main__":
	unittest.main()
