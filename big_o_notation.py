"""
Playing around with O(?)

"""

import time


def sum_product(xs: list):  # O(n)
    sum = 0
    product = 1

    for i in xs:
        sum += i
        product *= i

    print(f"Product:{product}, Sum:{sum}")


def print_pairs_1(xs: list):  # O(n^2) Nested loops are n^2 complexity
    for i in xs:
        for j in xs:
            print(f"i:{i}, j:{j}")


def print_pairs_2(xs: list):  # O((n^2)/2) because the nested loop always skips forward one index each time
    for i, num in enumerate(xs):
        for nxt_num in xs[i + 1 :]:
            print(f"i:{num}, j:{nxt_num}")


if __name__ == "__main__":
    t1 = time.perf_counter_ns()
    int_list = [10, 24, 4, 3, 20]
    # sum_product()
    print_pairs_1(int_list)
    # print_pairs_2(int_list)
    t2 = time.perf_counter_ns()
    print((t2 - t1) / 1000)
