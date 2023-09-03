def solution(n: int) -> tuple[tuple, tuple]:
	list_1 = tuple(n for _ in range(n))
	list_2 = tuple(n for _ in f"{n}")
	return (list_1, list_2) if len(list_1) < len(list_2) else (list_2, list_1)


def main(*args: str, **kwargs: str) -> str:
	if not kwargs:
		return "{}\n{}".format(*solution(int(args[0])))
	return "{}\n{}".format(*solution(int(kwargs["n"])))


if __name__ == "__main__":
	print(main(input()))
