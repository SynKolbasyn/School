import unittest
import src.Task_2


class Task2TestCase(unittest.TestCase):
	def test_solution(self):
		self.assertEqual(src.Task_2.solution(), None)

	def test_main(self):
		self.assertEqual(src.Task_2.main(), None)


if __name__ == "__main__":
	unittest.main()
