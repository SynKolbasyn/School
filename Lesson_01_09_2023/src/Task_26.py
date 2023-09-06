def solution(n: int) -> tuple[tuple[list[str], ...], tuple[str, ...]]:
	vasya = tuple([f"Character_{i}"] for i in range(n))
	alice = tuple(f"Character_{i}" for i in range(n))
	return vasya, alice


def main(*args: str, **kwargs: str) -> str:
	if kwargs:
		return "{}\n{}".format(*solution(n=int(kwargs["n"])))
	return "{}\n{}".format(*solution(int(args[0])))


if __name__ == "__main__":
	print(main(input()))
