def solution(n: int) -> str:
	result = ""
	old_result = ""
	for i in range(1, n + 1):
		result += f"{i}"
		if len(result) > n:
			return old_result
		old_result = result
	return result


def main(*args: str, **kwargs: str) -> str:
	if kwargs:
		return solution(n=int(kwargs["n"]))
	return solution(int(args[0]))


if __name__ == "__main__":
	print(main(input()))
