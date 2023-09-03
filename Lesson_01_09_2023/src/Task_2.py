def solution(s: int, v1: int, v2: int) -> float:
	return int(s / (v2 - v1))


def main(*args, **kwargs) -> float:
	if not kwargs:
		if len(args) == 1:
			return solution(*tuple(map(int, args[0].split())))
		return solution(*tuple(map(int, args)))
	return solution(s=int(kwargs["s"]), v1=int(kwargs["v1"]), v2=int(kwargs["v2"]))


if __name__ == "__main__":
	print(main(input()))
