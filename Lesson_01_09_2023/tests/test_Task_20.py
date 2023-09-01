import unittest
import src.Task_20


class Task20TestCase(unittest.TestCase):
	def test_solution(self):
		self.assertEqual(src.Task_20.solution(), None)

	def test_main(self):
		self.assertEqual(src.Task_20.main(), None)


if __name__ == "__main__":
	unittest.main()
