from random import sample
from math import ceil


def solution(matrix: list[list[int], ...]) -> tuple[int, list[int, ...]]:
    summa = 0
    odd_sum = [0 for _ in range(ceil(len(matrix) / 2))]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if j <= i:
                summa += matrix[i][j]
            if j % 2 == 0:
                odd_sum[j // 2] += matrix[i][j]
    return summa, odd_sum


def main(*args: str, **kwargs: str) -> str:
    matrix = [list(map(int, i.split())) for i in args]
    return "MATRIX:\n" + f"{matrix}".replace("], ", "]\n")[1:-1] + "\nSUMM: {}\nODD SUMM: {}".format(*solution(matrix))


if __name__ == "__main__":
    r = 3
    m = [sample(range(-r, r + 1), r) for _ in range(r)]
    print(main(*(f"{i}".replace("[", "").replace("]", "").replace(",", "") for i in m)))
