def solution(s: int, v1: int, v2: int) -> float:
	return int(s / (v2 - v1))


def main(*args: str, **kwargs: str) -> float:
	if kwargs:
		return solution(s=int(kwargs["s"]), v1=int(kwargs["v1"]), v2=int(kwargs["v2"]))
	if len(args) == 1:
		return solution(*map(int, args[0].split()))
	return solution(*map(int, args))


if __name__ == "__main__":
	print(main(input()))
