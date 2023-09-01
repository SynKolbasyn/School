import unittest
import src.Task_11


class Task11TestCase(unittest.TestCase):
	def test_solution(self):
		self.assertEqual(src.Task_11.solution(), None)

	def test_main(self):
		self.assertEqual(src.Task_11.main(), None)


if __name__ == "__main__":
	unittest.main()
