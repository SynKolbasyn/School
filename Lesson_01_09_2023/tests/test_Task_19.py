import unittest
import src.Task_19


class Task19TestCase(unittest.TestCase):
	def test_solution(self):
		self.assertEqual(src.Task_19.solution(("A", "B", "C", "A")), 3)

	def test_main_arg(self):
		self.assertEqual(src.Task_19.main("A B C A"), 3)

	def test_main_args(self):
		self.assertEqual(src.Task_19.main("A", "B", "C", "A"), 3)


if __name__ == "__main__":
	unittest.main()
