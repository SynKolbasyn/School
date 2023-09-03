def solution() -> str:
	return "12" * 12 + "У"


def main(*args: str, **kwargs: str) -> str:
	return solution()


if __name__ == "__main__":
	print(main())
