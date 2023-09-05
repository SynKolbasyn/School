def solution(string: str) -> str:
	message = ""
	for i in string.split():
		message += i[0]
	return message


def main(*args: str, **kwargs: str) -> str:
	return solution(args[0])


if __name__ == "__main__":
	print(main(input()))
