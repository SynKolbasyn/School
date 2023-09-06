from random import sample


def solution(array: list[int, ...]) -> tuple[int, int]:
    maximum = min(array)
    odd_count = 0
    for i in array:
        if i % 2 == 0 and i > maximum:
            maximum = i
        if i % 2 == 1 and i < 0:
            odd_count += 1
    return maximum, odd_count


def main(*args: str, **kwargs: str) -> str:
    if len(args) == 1:
        array = list(map(int, args[0].split()))
        return "ARRAY: {}\nMAX: {}\nODD COUNT: {}".format(array, *solution(array))
    array = list(map(int, args))
    return "ARRAY: {}\nMAX: {}\nODD COUNT: {}".format(array, *solution(array))


if __name__ == "__main__":
    r = 10
    print(main(*(f"{i}" for i in sample(range(-r, r + 1), r))))
