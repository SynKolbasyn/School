import unittest
import src.Task_17


class Task17TestCase(unittest.TestCase):
	def test_solution(self):
		self.assertEqual(src.Task_17.solution("Папа"), "П-п-")

	def test_main(self):
		self.assertEqual(src.Task_17.main("Папа"), "П-п-")


if __name__ == "__main__":
	unittest.main()
