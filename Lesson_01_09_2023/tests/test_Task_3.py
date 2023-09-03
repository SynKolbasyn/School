import unittest
import src.Task_3


class Task3TestCase(unittest.TestCase):
	def test_solution(self):
		self.assertEqual(src.Task_3.solution(10), ((10, 10), (10, 10, 10, 10, 10, 10, 10, 10, 10, 10)))

	def test_main(self):
		self.assertEqual(src.Task_3.main("10"), "(10, 10)\n(10, 10, 10, 10, 10, 10, 10, 10, 10, 10)")


if __name__ == "__main__":
	unittest.main()
