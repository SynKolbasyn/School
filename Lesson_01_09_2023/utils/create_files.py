import os


def create_folders(folders: tuple) -> None:
    for folder in folders:
        os.mkdir(folder)


def create_src(path_with_name: str) -> None:
    with open(path_with_name, "w") as file:
        file.write(
            "def solution() -> None:\n\t"
            "pass\n\n\n"
            "def main(*args, **kwargs) -> None:\n\t"
            "return solution()\n\n\n"
            "if __name__ == \"__main__\":\n\t"
            "print(main())\n"
        )


def create_tests(path: str, name: str) -> None:
    with open(path + name, "w") as file:
        file.write(
            "import unittest\n"
            f"import src.{name[5:-3]}\n\n\n"
            f"class {name[5:-3].replace('_', '')}TestCase(unittest.TestCase):\n\t"
            "def test_solution(self):\n\t\t"
            f"self.assertEqual(src.{name[5:-3]}.solution(), None)\n\n\t"
            "def test_main(self):\n\t\t"
            f"self.assertEqual(src.{name[5:-3]}.main(), None)\n\n\n"
            "if __name__ == \"__main__\":\n\t"
            "unittest.main()\n"
        )


def main() -> None:
    create_folders(("../src/", "../tests/"))
    for number in range(1, 26):
        create_src(f"../src/Task_{number}.py")
        create_tests("../tests/", f"test_Task_{number}.py")


if __name__ == "__main__":
    main()
