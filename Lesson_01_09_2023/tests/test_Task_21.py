import unittest
import src.Task_21


class Task21TestCase(unittest.TestCase):
	def test_solution(self):
		self.assertEqual(src.Task_21.solution("Hi eleven low level overview"), "Hello")

	def test_main_arg(self):
		self.assertEqual(src.Task_21.main("Hi eleven low level overview"), "Hello")


if __name__ == "__main__":
	unittest.main()
