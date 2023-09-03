def solution(a: int, b: int, d: int) -> int:
	misha_dot = a % d
	borya_dot = b % d
	misha = min(misha_dot, d - misha_dot)
	borya = min(borya_dot, d - borya_dot)
	return (a if misha < borya else b) if misha != borya else min(a, b)


def main(*args: str, **kwargs: str) -> int:
	if not kwargs:
		if len(args) == 1:
			return solution(*map(int, args[0].split()))
		return solution(*map(int, args))
	return solution(a=int(kwargs["a"]), b=int(kwargs["b"]), d=int(kwargs["d"]))


if __name__ == "__main__":
	print(main(input()))
