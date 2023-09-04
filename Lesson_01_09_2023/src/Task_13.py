def solution(x: int, y: int) -> int:
	if x < 0 and y < 0:
		return max(x + y, x ** y)
	if x < 0 == y:
		return max(x + y, x ** y, int(f"{x}{y}"))
	if y < 0 == x:
		return max(x + y, y ** x, int(f"{y}{x}"))
	return max(x + y, x ** y, y ** x, int(f"{x}{y}"), int(f"{y}{x}"))


def main(*args: str, **kwargs: str) -> int:
	if kwargs:
		return solution(x=int(kwargs["x"]), y=int(kwargs["y"]))
	if len(args) == 1:
		return solution(*map(int, args[0].split()))
	return solution(*map(int, args))


if __name__ == "__main__":
	print(main(input()))
