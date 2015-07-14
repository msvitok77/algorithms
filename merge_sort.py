"""
Merge sort implementation
"""

def merge_sort(a_list, left, right):
    """Main algorithm for merge sort"""
    if left < right:
        middle = (left + right) // 2
        merge_sort(a_list, left, middle)
        merge_sort(a_list, middle + 1, right)
        merge(a_list, left, middle, right)

def merge(a_list, left, middle, right):
    """Merges two halves together"""
    a_list_new = []
    i = left
    j = middle + 1

    while i <= middle and j <= right:
        if a_list[i] < a_list[j]:
            a_list_new.append(a_list[i])
            i += 1
        else:
            a_list_new.append(a_list[j])
            j += 1

    while i <= middle:
        a_list_new.append(a_list[i])
        i += 1

    while j <= left:
        a_list_new.append(a_list[j])
        j += 1

    for v in a_list_new:
        a_list[left] = v
        left += 1

if __name__ == '__main__':
    A_LIST = [8, 5, 3, 1, 9, 6, 0, 7, 4, 2, 5]
    merge_sort(A_LIST, 0, len(A_LIST) - 1)

    print A_LIST
