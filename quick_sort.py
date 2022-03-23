""" Quick sort algorithm """


def swap(a_list, first, second):
    """Swaps two values within the list"""
    a_list[first], a_list[second] = a_list[second], a_list[first]


def q_sort(a_list, left, right):
    """Quick sort algorithm"""
    if left < right:
        pivot = left
        pivot_val = a_list[pivot]
        for i in range(left + 1, right):
            if a_list[i] < pivot_val:
                pivot += 1
                swap(a_list, pivot, i)
        swap(a_list, pivot, left)
        q_sort(a_list, left, pivot)
        q_sort(a_list, pivot + 1, right)


if __name__ == '__main__':
    A_LIST = [8, 5, 3, 1, 9, 6, 0, 7, 4, 2, 5]
    q_sort(A_LIST, 0, len(A_LIST))
    print(A_LIST)
