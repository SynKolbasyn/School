def solution(number: int) -> list[int, ...]:
	answer = []
	for i in range(10):
		old_num = f"{number - i}{i}"
		if len(old_num) < 3:
			continue
		answer.append(int(old_num))
	return answer


def main(*args: str, **kwargs: str) -> str:
	answer = ""
	for i in solution(int(args[0])):
		if len(answer) == 0:
			answer = f"{i}"
			continue
		answer = f"{answer}\n{i}"
	return answer


if __name__ == "__main__":
	print(main(input()))
