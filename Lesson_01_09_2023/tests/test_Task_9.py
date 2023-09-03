import unittest
import src.Task_9


class Task9TestCase(unittest.TestCase):
	def test_solution_1(self):
		self.assertFalse(src.Task_9.solution(123, 456, 789))

	def test_solution_2(self):
		self.assertTrue(src.Task_9.solution(111, 111, 111))

	def test_main_1(self):
		self.assertEqual(src.Task_9.main("123", "456", "789"), "NO")

	def test_main_2(self):
		self.assertEqual(src.Task_9.main("111", "111", "111"), "YES")


if __name__ == "__main__":
	unittest.main()
