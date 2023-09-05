def solution(word: str) -> str:
	result = ""
	for i in word:
		if not (i in ("П", "п")):
			result += "-"
			continue
		result += i
	return result


def main(*args: str, **kwargs: str) -> str:
	return solution(args[0])


if __name__ == "__main__":
	print(main(input()))
