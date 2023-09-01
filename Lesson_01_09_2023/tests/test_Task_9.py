import unittest
import src.Task_9


class Task9TestCase(unittest.TestCase):
	def test_solution(self):
		self.assertEqual(src.Task_9.solution(), None)

	def test_main(self):
		self.assertEqual(src.Task_9.main(), None)


if __name__ == "__main__":
	unittest.main()
