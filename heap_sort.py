"""
Heap sort implementation
"""
def swap(a_list, first, second):
    """Swaps two values within the list"""
    a_list[first], a_list[second] = a_list[second], a_list[first]

def heap_sort(a_list):
    """Main algorithm for heap sort"""
    length = len(a_list) - 1
    # index of node which is the last parent (has child/ children)
    last_parent = length / 2

    for i in range(last_parent, -1, -1):
        heapify(a_list, i, length)

    # put max value to the end and shorten array and heapify again
    for i in range(length, 0, -1):
        if a_list[0] > a_list[i]:
            swap(a_list, 0, i)
            heapify(a_list, 0, i - 1)

def heapify(a_list, first, last):
    """Rebuild the heap"""
    # left child
    max_idx = first * 2 + 1
    while max_idx <= last:
        if (max_idx < last) and (a_list[max_idx] < a_list[max_idx + 1]):
            # right child
            max_idx += 1

        if a_list[first] < a_list[max_idx]:
            swap(a_list, first, max_idx)
            first = max_idx
            max_idx = first * 2 + 1
        else:
            break


if __name__ == '__main__':
    A_LIST = [8, 5, 3, 1, 9, 6, 0, 7, 4, 2, 5]
    heap_sort(A_LIST)
    print A_LIST
