import unittest
import src.Task_3


class Task3TestCase(unittest.TestCase):
	def test_solution(self):
		self.assertEqual(src.Task_3.solution(), None)

	def test_main(self):
		self.assertEqual(src.Task_3.main(), None)


if __name__ == "__main__":
	unittest.main()
