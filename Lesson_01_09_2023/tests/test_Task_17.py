import unittest
import src.Task_17


class Task17TestCase(unittest.TestCase):
	def test_solution(self):
		self.assertEqual(src.Task_17.solution(), None)

	def test_main(self):
		self.assertEqual(src.Task_17.main(), None)


if __name__ == "__main__":
	unittest.main()
