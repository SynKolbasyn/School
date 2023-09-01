import unittest
import src.Task_7


class Task7TestCase(unittest.TestCase):
	def test_solution(self):
		self.assertEqual(src.Task_7.solution(), None)

	def test_main(self):
		self.assertEqual(src.Task_7.main(), None)


if __name__ == "__main__":
	unittest.main()
