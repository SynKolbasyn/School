import unittest
import src.Task_23


class Task23TestCase(unittest.TestCase):
	def test_solution_1(self):
		self.assertEqual(src.Task_23.solution("ВасяВасяАлисаАлисаАлисаЯ"), "Алиса")

	def test_solution_2(self):
		self.assertEqual(src.Task_23.solution("ВасяВасяАлисаАлисаАлисаЯЯЯЯЯ"), "Соня")

	def test_main_arg_1(self):
		self.assertEqual(src.Task_23.main("ВасяВасяАлисаАлисаАлисаЯ"), "Алиса")

	def test_main_arg_2(self):
		self.assertEqual(src.Task_23.main("ВасяВасяАлисаАлисаАлисаЯЯЯЯЯ"), "Соня")


if __name__ == "__main__":
	unittest.main()
