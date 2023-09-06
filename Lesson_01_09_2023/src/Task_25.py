def solution(string: str) -> bool:
	old_char = "a"
	string = string.lower()
	for i in string:
		if i < old_char:
			return False
		old_char = i
	return True


def main(*args: str, **kwargs: str) -> str:
	return "YES" if solution(args[0]) else "NO"


if __name__ == "__main__":
	print(main(input()))
