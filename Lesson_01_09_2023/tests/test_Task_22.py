import unittest
import src.Task_22


class Task22TestCase(unittest.TestCase):
	def test_solution(self):
		self.assertEqual(src.Task_22.solution(), None)

	def test_main(self):
		self.assertEqual(src.Task_22.main(), None)


if __name__ == "__main__":
	unittest.main()
