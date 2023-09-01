import unittest
import src.Task_19


class Task19TestCase(unittest.TestCase):
	def test_solution(self):
		self.assertEqual(src.Task_19.solution(), None)

	def test_main(self):
		self.assertEqual(src.Task_19.main(), None)


if __name__ == "__main__":
	unittest.main()
