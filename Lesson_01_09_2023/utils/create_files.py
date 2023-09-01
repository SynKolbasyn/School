import os


def create_folders(folders: tuple) -> None:
    for folder in folders:
        os.mkdir(folder)


def create_src(path_with_name: str) -> None:
    pass


def create_tests(path: str, name: str) -> None:
    pass


def main() -> None:
    create_folders(("../src/", "../tests/"))
    for number in range(1, 26):
        create_src(f"../src/Task_{number}.py")
        create_tests("../tests/", f"test_Task_{number}.py")


if __name__ == "__main__":
    main()
