def solution(b: int, c: int, d: int) -> int:
	return 3 - (b + c + d) % 3


def main(*args: str, **kwargs: str) -> int:
	if kwargs:
		return solution(b=int(kwargs["b"]), c=int(kwargs["c"]), d=int(kwargs["d"]))
	if len(args) == 1:
		return solution(*map(int, args[0].split()))
	return solution(*map(int, args))


if __name__ == "__main__":
	print(main(input()))
