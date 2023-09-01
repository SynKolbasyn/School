import unittest
import src.Task_21


class Task21TestCase(unittest.TestCase):
	def test_solution(self):
		self.assertEqual(src.Task_21.solution(), None)

	def test_main(self):
		self.assertEqual(src.Task_21.main(), None)


if __name__ == "__main__":
	unittest.main()
