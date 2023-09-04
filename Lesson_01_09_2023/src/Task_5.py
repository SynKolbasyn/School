def solution(n: int) -> str:
	if n % len(f"{n}") != 0:
		return "IMPOSSIBLE"
	result = ""
	while len(result) != n:
		result += f"{n}"
	return result


def main(*args: str, **kwargs: str) -> str:
	if kwargs:
		return solution(int(kwargs["n"]))
	return solution(int(args[0]))


if __name__ == "__main__":
	print(main(input()))
