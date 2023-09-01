import unittest
import src.Task_4


class Task4TestCase(unittest.TestCase):
	def test_solution(self):
		self.assertEqual(src.Task_4.solution(), None)

	def test_main(self):
		self.assertEqual(src.Task_4.main(), None)


if __name__ == "__main__":
	unittest.main()
