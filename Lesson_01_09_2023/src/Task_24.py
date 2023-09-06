def solution(string: str, n: int) -> str:
	result = ""
	iterations = (len(string) - n) // (n + 1)
	for i in range(iterations):
		result += string[(i + 1) * (n + 1) - 1]
	return result


def main(*args: str, **kwargs: str) -> str:
	if len(args) == 1:
		string, n = args[0].split()
		return solution(string, int(n))
	return solution(args[0], int(args[1]))


if __name__ == "__main__":
	print(main(input()))
