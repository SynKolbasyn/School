import unittest
import src.Task_10


class Task10TestCase(unittest.TestCase):
	def test_solution(self):
		self.assertEqual(src.Task_10.solution(), None)

	def test_main(self):
		self.assertEqual(src.Task_10.main(), None)


if __name__ == "__main__":
	unittest.main()
