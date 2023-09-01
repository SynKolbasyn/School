import unittest
import src.Task_18


class Task18TestCase(unittest.TestCase):
	def test_solution(self):
		self.assertEqual(src.Task_18.solution(), None)

	def test_main(self):
		self.assertEqual(src.Task_18.main(), None)


if __name__ == "__main__":
	unittest.main()
