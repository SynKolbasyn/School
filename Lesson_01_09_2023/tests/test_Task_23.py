import unittest
import src.Task_23


class Task23TestCase(unittest.TestCase):
	def test_solution(self):
		self.assertEqual(src.Task_23.solution(), None)

	def test_main(self):
		self.assertEqual(src.Task_23.main(), None)


if __name__ == "__main__":
	unittest.main()
