def solution(array: tuple[int, ...]) -> list[int]:
	n = len(array)
	result = []
	for i in array:
		if i % n == 0:
			result.append(i)
	return result


def make_str(array: list[int, ...]) -> str:
	result = ""
	for i in array:
		if result == "":
			result = f"{i}"
			continue
		result = f"{result}\n{i}"
	return result


def main(*args: str, **kwargs: str) -> str:
	if len(args) == 1:
		return make_str(solution(tuple(map(int, args[0].split()))))
	return make_str(solution(tuple(map(int, args))))


if __name__ == "__main__":
	print(main(input()))
