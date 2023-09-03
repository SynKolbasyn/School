import unittest
import src.Task_4


class Task4TestCase(unittest.TestCase):
	def test_solution_1(self):
		self.assertEqual(src.Task_4.solution(10), [100])

	def test_solution_2(self):
		self.assertEqual(src.Task_4.solution(99), [990, 981, 972, 963, 954, 945, 936, 927, 918, 909])

	def test_main_1(self):
		self.assertEqual(src.Task_4.main("10"), "100")

	def test_main_2(self):
		self.assertEqual(src.Task_4.main("99"), "990\n981\n972\n963\n954\n945\n936\n927\n918\n909")


if __name__ == "__main__":
	unittest.main()
