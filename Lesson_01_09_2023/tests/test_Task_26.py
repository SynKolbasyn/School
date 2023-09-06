import unittest
import src.Task_26


class Task25TestCase(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(src.Task_26.solution(2), ((["Character_0"], ["Character_1"]), ("Character_0", "Character_1")))

    def test_main_arg(self):
        self.assertEqual(src.Task_26.main("2"), "(['Character_0'], ['Character_1'])\n('Character_0', 'Character_1')")

    def test_main_kwargs(self):
        self.assertEqual(src.Task_26.main(n="2"), "(['Character_0'], ['Character_1'])\n('Character_0', 'Character_1')")


if __name__ == "__main__":
    unittest.main()
