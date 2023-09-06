from random import sample


def solution(matrix: list[list[int, ...], ...]) -> tuple[int, list[int, ...]]:
    count = 0
    max_num_in_matrix = max([max(i) for i in matrix])
    minimum = [max_num_in_matrix for _ in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if j >= len(matrix) - i - 1:
                count += matrix[i][j] % 10 == 0
            minimum[j] = min(abs(matrix[i][j]), minimum[j])
    return count, minimum


def main(*args: str, **kwargs: str) -> str:
    matrix = [list(map(int, i.split())) for i in args]
    return "MATRIX:\n" + f"{matrix}".replace("], ", "]\n")[1:-1] + "\nCOUNT: {}\nMINIMUM: {}".format(*solution(matrix))


if __name__ == "__main__":
    r = 3
    m = [sample(range(-r, r + 1), r) for _ in range(r)]
    print(main(*(f"{i}".replace("[", "").replace("]", "").replace(",", "") for i in m)))
