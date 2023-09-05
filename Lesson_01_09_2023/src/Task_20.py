def solution(string: str) -> str:
	result = ""
	old_char = ""
	for i in string:
		if (i != old_char) and (old_char != ""):
			result += " "
		result += i
		old_char = i
	return result


def main(*args: str, **kwargs: str) -> str:
	return solution(args[0])


if __name__ == "__main__":
	print(main(input()))
