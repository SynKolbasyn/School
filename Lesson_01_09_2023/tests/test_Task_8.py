import unittest
import src.Task_8


class Task8TestCase(unittest.TestCase):
	def test_solution(self):
		self.assertEqual(src.Task_8.solution(), None)

	def test_main(self):
		self.assertEqual(src.Task_8.main(), None)


if __name__ == "__main__":
	unittest.main()
