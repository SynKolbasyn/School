def solution(a: int, b: int, c: int, n: int) -> tuple[float, float, float]:
	cycle_time = a + b + c + b
	cycles_count = n / cycle_time
	red = (a + b) * cycles_count
	yellow = (b + b) * cycles_count
	green = c * cycles_count
	return red, yellow, green


def main(*args: str, **kwargs: str) -> str:
	if kwargs:
		return "Red: {}\nYellow: {}\nGreen: {}".format(*solution(
			a=int(kwargs["a"]),
			b=int(kwargs["b"]),
			c=int(kwargs["c"]),
			n=int(kwargs["n"])
		))
	if len(args) == 1:
		return "Red: {}\nYellow: {}\nGreen: {}".format(*solution(*map(int, args[0].split())))
	return "Red: {}\nYellow: {}\nGreen: {}".format(*solution(*map(int, args)))


if __name__ == "__main__":
	print(main(input()))
