def solution(road_1: str, road_2: str) -> int:
	road_1_rate = 3 if road_1.lower() == "cat" else (2 if road_1.lower() == "pigeon" else 1)
	road_2_rate = 3 if road_2.lower() == "cat" else (2 if road_2.lower() == "pigeon" else 1)
	return 1 if road_1_rate >= road_2_rate else 2


def main(*args: str, **kwargs: str) -> int:
	if len(args) == 1:
		return solution(*args[0].split())
	return solution(args[0], args[1])


if __name__ == "__main__":
	print(main(input()))
