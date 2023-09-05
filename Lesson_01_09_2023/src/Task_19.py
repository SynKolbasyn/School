def solution(stations: tuple[str, ...]) -> int:
	past_stations = []
	for i in stations:
		if i in past_stations:
			return len(past_stations)
		past_stations.append(i)
	return len(past_stations)


def main(*args: str, **kwargs: str) -> int:
	if len(args) == 1:
		return solution(tuple(args[0].split()))
	return solution(args)


if __name__ == "__main__":
	print(main(input()))
