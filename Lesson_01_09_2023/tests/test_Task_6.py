import unittest
import src.Task_6


class Task6TestCase(unittest.TestCase):
	def test_solution(self):
		self.assertEqual(src.Task_6.solution(), None)

	def test_main(self):
		self.assertEqual(src.Task_6.main(), None)


if __name__ == "__main__":
	unittest.main()
