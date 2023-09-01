import unittest
import src.Task_12


class Task12TestCase(unittest.TestCase):
	def test_solution(self):
		self.assertEqual(src.Task_12.solution(), None)

	def test_main(self):
		self.assertEqual(src.Task_12.main(), None)


if __name__ == "__main__":
	unittest.main()
