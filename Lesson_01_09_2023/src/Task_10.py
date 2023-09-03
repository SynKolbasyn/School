def solution(l1: int, r1: int, l2: int, r2: int) -> bool:
	return r1 >= l2 and l1 <= r2


def main(*args: str, **kwargs: str) -> str:
	if not kwargs:
		if len(args) == 1:
			return "YES" if solution(*map(int, args[0].split())) else "NO"
		return "YES" if solution(*map(int, args)) else "NO"
	return "YES" if solution(
		l1=int(kwargs["l1"]),
		r1=int(kwargs["r1"]),
		l2=int(kwargs["l2"]),
		r2=int(kwargs["r2"])) else "NO"


if __name__ == "__main__":
	print(main(input()))
