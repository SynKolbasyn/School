def solution(string: str) -> str:
	vasya = string.count("Вася")
	alice = string.count("Алиса")
	i = string.count("Я")
	vinner = max(vasya, alice, i)
	if vinner == vasya:
		return "Вася"
	if vinner == alice:
		return "Алиса"
	if vinner == i:
		return "Соня"


def main(*args: str, **kwargs: str) -> str:
	return solution(args[0])


if __name__ == "__main__":
	print(main(input()))
