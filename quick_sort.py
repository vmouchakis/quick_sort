def quick_sort(sequence):
    length = len(sequence)          # we use a list as a sequence 
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()      # we take as pivot the last character of the list

    items_lower = []
    items_greater = []

    for item in sequence:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)


print(quick_sort([3, 5, 1, 7, 4, 8]))

# Complexity O(n^2)
