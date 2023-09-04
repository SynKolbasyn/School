def solution(n: int, x: int) -> int:
	override = x % n
	return min(override, n - override)


def main(*args: str, **kwargs: str) -> int:
	if kwargs:
		return solution(n=int(kwargs["n"]), x=int(kwargs["x"]))
	if len(args) == 1:
		return solution(*map(int, args[0].split()))
	return solution(*map(int, args))


if __name__ == "__main__":
	print(main(input()))
