def solution(row_1: int, row_2: int, row_3: int) -> bool:
	matrix = [[], [], []]
	for i in range(3):
		matrix[0].append(int(f"{row_1}"[i]))
		matrix[1].append(int(f"{row_2}"[i]))
		matrix[2].append(int(f"{row_3}"[i]))
	raw_sum = tuple(sum(i) for i in matrix)
	column_sum = tuple(sum(i) for i in zip(*matrix))
	diagonal_sum = (sum(matrix[i][i] for i in range(3)), sum(matrix[i][2 - i] for i in range(3)))
	return raw_sum[1:] == diagonal_sum if raw_sum == column_sum else False


def main(*args: str, **kwargs: str) -> str:
	return "YES" if solution(*map(int, args)) else "NO"


if __name__ == "__main__":
	print(main(input(), input(), input()))
