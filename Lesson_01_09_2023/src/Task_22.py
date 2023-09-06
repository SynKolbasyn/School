def solution(games: tuple[tuple[int, int], ...]) -> bool:
	for a, v in games:
		if a > v:
			return True
	return False


def main(*args: str, **kwargs: str) -> str:
	return "YES" if solution(tuple(tuple(map(int, i.split())) for i in args)) else "NO"


if __name__ == "__main__":
	print(main(input(), input()))
