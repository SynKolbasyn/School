def solution(a: int, b: int, r: int, u: int) -> tuple[int, str]:
	horizontal = min(a - r, r)
	vertical = min(b - u, u)
	steps = horizontal + vertical
	way = "R" * r + "U" * u + ("L" if horizontal == r else "R") * horizontal + ("D" if vertical == u else "U") * vertical
	return steps, way


def main(*args: str, **kwargs: str) -> str:
	if kwargs:
		steps, way = solution(a=int(kwargs["a"]), b=int(kwargs["b"]), r=int(kwargs["r"]), u=int(kwargs["u"]))
		return f"{steps}\n{way}"
	if len(args) == 1:
		steps, way = solution(*map(int, args[0].split()))
		return f"{steps}\n{way}"
	steps, way = solution(*map(int, args))
	return f"{steps}\n{way}"


if __name__ == "__main__":
	print(main(input()))
