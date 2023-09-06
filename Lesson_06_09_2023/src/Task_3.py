from random import sample


def solution(array: list[int, ...]) -> tuple[int, int]:
    after_minimum_count = -1
    after_maximum_count = -1
    minimum = min(array)
    maximum = max(array)
    is_find_minimum = False
    is_find_maximum = False
    for i in array:
        if not is_find_minimum:
            is_find_minimum = minimum == i
        if not is_find_maximum:
            is_find_maximum = maximum == i
        if is_find_minimum:
            after_minimum_count += 1
        if is_find_maximum:
            after_maximum_count += 1
    return after_minimum_count, after_maximum_count


def main(*args: str, **kwargs: str) -> str:
    if len(args) == 1:
        return "ARRAY: {}\nAFTER MIN: {}\nAFTER MAX: {}".format(list(map(int, args[0].split())), *solution(list(map(int, args[0].split()))))
    return "ARRAY: {}\nAFTER MIN: {}\nAFTER MAX: {}".format(list(map(int, args)), *solution(list(map(int, args))))


if __name__ == "__main__":
    r = 10
    print(main(f"{sample(range(-r, r + 1), r)}".replace("[", "").replace("]", "").replace(",", "")))
