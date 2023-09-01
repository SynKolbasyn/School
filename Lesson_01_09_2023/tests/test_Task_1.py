import unittest
import src.Task_1


class Task1TestCase(unittest.TestCase):
	def test_solution(self):
		self.assertEqual(src.Task_1.solution(), "121212121212121212121212У")

	def test_main(self):
		self.assertEqual(src.Task_1.main(), "121212121212121212121212У")


if __name__ == "__main__":
	unittest.main()
