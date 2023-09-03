import unittest
import src.Task_11


class Task11TestCase(unittest.TestCase):
	def test_solution_1(self):
		self.assertEqual(src.Task_11.solution(1), "Стол")

	def test_solution_2(self):
		self.assertEqual(src.Task_11.solution(2), "Стола")

	def test_solution_3(self):
		self.assertEqual(src.Task_11.solution(5), "Столов")

	def test_solution_4(self):
		self.assertEqual(src.Task_11.solution(11), "Столов")

	def test_solution_5(self):
		self.assertEqual(src.Task_11.solution(12), "Столов")

	def test_main_1(self):
		self.assertEqual(src.Task_11.main("1"), "Стол")

	def test_main_2(self):
		self.assertEqual(src.Task_11.main("2"), "Стола")

	def test_main_3(self):
		self.assertEqual(src.Task_11.main("5"), "Столов")

	def test_main_4(self):
		self.assertEqual(src.Task_11.main("11"), "Столов")

	def test_main_5(self):
		self.assertEqual(src.Task_11.main("12"), "Столов")


if __name__ == "__main__":
	unittest.main()
