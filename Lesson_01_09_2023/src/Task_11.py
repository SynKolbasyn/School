def solution(number: int) -> str:
	if 10 < number < 20:
		return "Столов"
	end = number % 10
	if end == 1:
		return "Стол"
	if 1 < end < 5:
		return "Стола"
	return "Столов"


def main(*args: str, **kwargs: str) -> str:
	return solution(int(args[0]))


if __name__ == "__main__":
	print(main(input()))
