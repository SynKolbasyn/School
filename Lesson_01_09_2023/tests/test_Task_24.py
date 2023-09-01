import unittest
import src.Task_24


class Task24TestCase(unittest.TestCase):
	def test_solution(self):
		self.assertEqual(src.Task_24.solution(), None)

	def test_main(self):
		self.assertEqual(src.Task_24.main(), None)


if __name__ == "__main__":
	unittest.main()
