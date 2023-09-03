import unittest
import src.Task_5


class Task5TestCase(unittest.TestCase):
	def test_solution(self):
		self.assertEqual(src.Task_5.solution(10), "1010101010")

	def test_solution_impossible(self):
		self.assertEqual(src.Task_5.solution(11), "IMPOSSIBLE")

	def test_main(self):
		self.assertEqual(src.Task_5.main("10"), "1010101010")

	def test_main_impossible(self):
		self.assertEqual(src.Task_5.main("11"), "IMPOSSIBLE")


if __name__ == "__main__":
	unittest.main()
