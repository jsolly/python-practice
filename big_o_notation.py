"""
Playing around with O(?)

"""

import time
from binarytree import tree


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


def print_pairs_2(
    xs: list,
):  # O((n^2)/2) because the nested loop always skips forward one index each time
    for i, num in enumerate(xs):
        for nxt_num in xs[i + 1 :]:
            print(f"i:{num}, j:{nxt_num}")


def print_pairs_3(
    xs: list, ys: list
):  # O((a*b)/2) It's not n^2 because a and b could be different lengths
    for i, num in enumerate(xs):
        for nxt_num in ys[i + 1 :]:
            print(f"i:{num}, j:{nxt_num}")

# a = length of array
# s = length of a string
def sort_strings_in_array(arr:list): # O(a*s(log a + log s))
    new_arr = []
    for s in arr: # Going through each string in the array is O(a)
        new_arr.append(''.join(sorted(s))) # Sorting each string is O(s log s)

    # Sorting the final array of strings is O(a log a), but don't forget we have to compare each string which is O(s)
    print (sorted(new_arr))



def sum_node(node, acc):
    if not node:
        return acc
    else:
        left_node = node.left if node.left else []
        right_node = node.right if node.right else []
        result = node.value + sum_node(left_node, acc) + sum_node(right_node, acc)
        return result

def sum_node_tr(node): # Tail recursive
    if not node:
        return 0

    def fn_for_node(node, todo, acc):
        todo = todo + list(filter(None,[node.left, node.right]))
        return fn_for_lon(todo, acc + node.value)

    def fn_for_lon(todo, acc):
        if not todo:
            print(acc)
        else:
            fn_for_node(todo[0], todo[1:], acc)

    return fn_for_node(node, [], 0)

if __name__ == "__main__":
    t1 = time.perf_counter_ns()
    int_list = [10, 24, 4, 3, 20]
    int_list_2 = [10, 24, 4, 3, 20]
    str_list = ["apples", "pears", "peaches", "bananas"]
    # sum_product()
    #print_pairs_3(int_list, int_list_2)
    #print_pairs_2(int_list)
    #sort_strings_in_array(str_list)

    ### Binary Trees
    my_tree = tree(height=9, is_perfect=False)
    sum_node_tr(my_tree)
    t2 = time.perf_counter_ns()
    print(f"Ran in {(t2 - t1) / 1000} miliseconds")
